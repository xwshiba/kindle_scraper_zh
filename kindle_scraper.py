"""
Project:    Kindle Scraper for Mandarin System
Started:    19/02/2020
Summary:    Scrape your highlights from Kindle's My Clippings.txt
"""

from sys import argv
from csv import writer, DictWriter

my_clippings = 'My Clippings.txt'  # filename.


def getLines():
    "Returns list of all lines from file. Extra delimeter is added to beginning."
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
        "Returns tuple (kind_of_unit, location). For locations of type '100-123', we take 100."
        listed_details = details.split()
        return(f"Location {listed_details[2].split('-')[0].split('#')[1]}")

    lines, units = getLines(), []

    for delimeterIndex in delimeterIndices():
        title = lines[delimeterIndex+1]
        # (highlight/note/bookmark, location)
        details = parseDetails(lines[delimeterIndex+2])
        message = lines[delimeterIndex+4]
        units.append((title, details, message))
    return units


def getTitles():
    "Returns alphabetically sorted list of titles. Removes duplicates."
    # to-do: allow sorting using keys- last read or alphabetically.
    from string import ascii_letters
    titles = []
    for unit in units:
        title = unit[0]
        # handling titles that start with u'\ufeff'.
        if title[0] not in ascii_letters:
            titles.append(title[1:])
        else:
            titles.append(title)
    return sorted(list(set(titles)))


def titleScraper(title):
    """remove special characters " /\: *?"<>|" based on .txt filename restrictions"""
    regex = r'/\\\\: \\*\\?"<>\\|'
    cleanTitle = title.translate({ord(c): "_" for c in regex})
    return cleanTitle


def help():
    features = {'showTitles': 'Show all the titles in your clipping.',
                'importAsTxt': 'Import your highlights as .txt in the same folder.',
                'importAsCsv': 'Import your highlights as .txt in the same folder.'}
    # 'importAsJSON': 'Import your highlights as JSON.'

    print("Welcome to kindler.py, use me to scrape your highlights from Kindle's My Clippings.txt \n")
    print("Here are commands and their descriptions: \n")

    for command, description in features.items():
        print(f"{command} : {description}")


def showTitles():
    "Prints all titles."
    [print(i, title) for i, title in enumerate(getTitles(), start=1)]


def informationFrom(title):
    "Returns list of all highlights in given title."
    matching_units = filter((lambda unit: title in unit[0]), units)
    temp = sorted(matching_units, key=(lambda x: x[1][1]))
    locations = [unit[1] for unit in temp]
    highlights = [unit[2] for unit in temp]
    return locations, highlights


def importAsTxt():
    "Imports your clippings as txt file, saves them in ../{title}.txt"

    for title in getTitles():
        cleanTitle = titleScraper(title)
        with open(f"{cleanTitle}.txt", "w+", encoding="utf-8") as outfile:
            locations = informationFrom(title)[0]
            highlights = informationFrom(title)[1]
            for index in range(0, len(locations)):
                outfile.write(f"{locations[index]} | {highlights[index]}")
                outfile.write('\n\n')

    print(
        f"I've saved {len(units)} highlights, notes and bookmarks from {len(getTitles())} titles in the same folder. You're welcome!")


def importAsCsv():
    "Imports your clippings as txt file, saves them in ../{title}.csv"
    for title in getTitles():
        cleanTitle = titleScraper(title)
        with open(f"{cleanTitle}.csv", "w+", encoding="utf-8") as outfile:
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
    print("Open Excel\nClick on the Data menu bar option\nClick on the From Text icon.\nNavigate to the location of the file that you want to import.\nClick on the filename and then click on the Import button.  The Text Import Wizard - Step 1 or 3 window will now appear on the screen.\nChoose the file type that best describes your data - Delimited or Fixed Width.\nChoose 65001: Unicode(UTF-8) from the drop-down list that appears next to File origin.\nChoose the appropriate data format for each column of data that you want to import. You also have the option to not import one or more columns of data if you want.\nClick on the Finish button to finish importing your data into Microsoft Excel.\nYou are welcome!"
          )


# def importAsJSON():
#     return None


if __name__ == "__main__":
    option = argv[1]

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
                print('Invalid option! For help, run: python kindler.py help')
        except FileNotFoundError:
            print(
                "Kindler: I can't find your My Clippings.txt file here. Did you paste it? \n")
