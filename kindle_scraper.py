"""
Project:    kindle_scraper for Mandarin System
Started:    19/02/2020
Summary:    Scrape your highlights from Kindle's My Clippings.txt
"""

from sys import argv
from csv import writer, DictWriter
import os

my_clippings = 'My Clippings.txt'  # filename.


def getLines():
    """Returns list of all lines from file. Extra delimeter is added to beginning."""
    file = open(my_clippings, 'r', encoding='utf-8')
    # can avoid extra delimeter by indexing properly
    return ['=========='] + [line.strip() for line in file]


def getUnits():
    """Returns list of all 'units'.
    A unit is a tuple with (title, details, message), NOT a highlight. Highlights and notes are messages."""

    def delimeterIndices(delimeter='=========='):
        "Returns indices of lines with delimeter. We use this to identify individual highlights."
        lines = getLines()  # why call getLines() twice?
        return [i for i, line in enumerate(lines) if line == '==========' and i != len(lines)-1]
        # if no extra delimeter in getLines(), last condition is just len(lines). Which is easier to read?

    def parseDetails(details):
        """Returns integer for location. For locations of type '100-123', we take 100. 
        And page information is eliminated."""
        listed_details = details.split()

        if '您在第' in listed_details[1] and '#' in listed_details[4]:
            location = listed_details[4].split('-')[0].split('#')[1]

        elif '您在第' not in listed_details[1]:
            # for extrem cases: only one number in location
            if '-' in listed_details[2]:
                location = listed_details[2].split('#')[1].split('-')[0]
            elif '的' in listed_details[2]:
                location = listed_details[2].split('#')[1][0:-3]
            else:
                location = listed_details[2].split('#')[1]
        else:
            location = 0

        return(int(location))

    lines, units = getLines(), []

    for delimeterIndex in delimeterIndices():
        title = lines[delimeterIndex+1]
        # (highlight/note/bookmark, location)
        details = parseDetails(lines[delimeterIndex+2])
        message = lines[delimeterIndex+4]
        # For extrem cases when message doesn't exist
        if message != "":
            units.append((title, details, message))
    return units


def getTitles():
    """Returns alphabetically sorted list of titles. Removes duplicates."""
    # to-do: allow sorting using keys- last read or alphabetically.
    from string import ascii_letters
    titles = []
    for unit in units:
        title = unit[0]
        titles.append(title)
    return sorted(list(set(titles)))


def titleScraper(title):
    """remove special symbols "/\: *?"<>|" based on .txt filename restrictions"""
    regex = r'/\\\\: \\*\\?"<>\\|'
    cleanTitle = title.translate({ord(c): "_" for c in regex})
    return cleanTitle


def help():
    features = {'showTitles': 'Show all the titles in your clipping.',
                'importAsTxt': 'Import your highlights as .txt in the same folder.',
                'importAsCsv': 'Import your highlights as .txt in the same folder.'}
    # 'importAsJSON': 'Import your highlights as JSON.'

    print("Welcome to kindle_scraper.py, use me to scrape your highlights from Kindle's My Clippings.txt \n")
    print("Here are commands and their descriptions: \n")

    for command, description in features.items():
        print(f"{command} : {description}")


def showTitles():
    """Prints all titles."""
    [print(i, title) for i, title in enumerate(getTitles(), start=1)]


def informationFrom(title):
    """Returns list of all highlights in given title."""
    # filter all the titles out
    matching_units = filter((lambda unit: title in unit[0]), units)
    temp = sorted(matching_units, key=(lambda x: x[1]))
    locations = [unit[1] for unit in temp]
    highlights = [unit[2] for unit in temp]
    return locations, highlights


def makeFile():
    cwd = os.path.abspath(os.curdir)
    directory = f'{cwd}/highlights'
    if not os.path.exists(directory):
        os.makedirs(directory)


def importAsTxt():
    """Imports your clippings as txt file, saves them in ../{title}.txt"""

    makeFile()

    for title in getTitles():
        cleanTitle = titleScraper(title)
        with open(f"highlights/{cleanTitle}.txt", "w+", encoding="utf-8") as outfile:
            locations = informationFrom(title)[0]
            highlights = informationFrom(title)[1]
            for index in range(0, len(locations)):
                outfile.write(f"{locations[index]} | {highlights[index]}")
                outfile.write('\n\n')

    print(
        f"I've saved {len(units)} highlights, notes and bookmarks from {len(getTitles())} titles in the same folder. You're welcome!")


def importAsCsv():
    """Imports your clippings as txt file, saves them in ../{title}.csv"""

    makeFile()

    for title in getTitles():
        cleanTitle = titleScraper(title)
        with open(f"highlights/{cleanTitle}.csv", "w+", encoding="utf-8") as outfile:
            headers = ["Location", "Highlights"]
            csv_writer = DictWriter(outfile, fieldnames=headers)
            csv_writer.writeheader()
            locations = informationFrom(title)[0]
            highlights = informationFrom(title)[1]
            for index in range(0, len(locations)):
                csv_writer.writerow({
                    "Location": locations[index],
                    "Highlights": highlights[index]
                })
    print(
        f"I've saved {len(units)} highlights, notes and bookmarks from {len(getTitles())} titles in the same folder. Please read the instructions here for open the .csv files:\n")

    print("============Instructions============\n1. Open an empty Microsoft Excel File;\n2. Click on the 'Data' menu bar option\n3. Click on the From Text icon.\n4. Navigate to the location of the file that you want to import.\n5. Click on the filename and then click on the Import button.\n6.The Text Import Wizard - Step 1 or 3 window will now appear on the screen.\n7. Choose the file type that best describes your data - 'Delimited'.\n8. Choose '65001: Unicode(UTF-8)' from the drop-down list that appears next to File origin.\n9. Choose the 'comma' as delimeter.\n10. Choose to open as a new sheet. \n11. Click on the Finish button to finish importing your data into Microsoft Excel.\n12. You are welcome!"
          )


# def importAsJSON():
#     return None


if __name__ == "__main__":
    try:
        option = argv[1]
    except IndexError:
        option = 'help'

    modes = {'showTitles': showTitles,
             'importAsTxt': importAsTxt, 'importAsCsv': importAsCsv}
    #  'importAsJSON': importAsJSON}

    if option == 'help':
        help()
    else:
        try:
            units = getUnits()
            try:
                outputs = modes[option]()
            except KeyError:
                print('Invalid option! For help, run: python kindle_scraper.py help')
        except FileNotFoundError:
            print(
                "Kindle_scraper: I can't find your My Clippings.txt file here. Did you paste it? \n")
