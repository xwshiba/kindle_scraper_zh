## Kindle Scraper for Mandarin System

_Latest Update on Aug, 2021: fixed the command line error in the terminal_

Using Python to organize Kindle's `My Clippings.txt`. It will generate individual .csv or .txt files for each book, which contains highlights and notes with sorted location information. You can use the exported .csv and .txt files in any personal notebook platforms, such as Notion and Evernote.  
__For User Guide written in Mandarin and reflections of building this script, please visit my personal blog [Shiba Woof's Playground](https://www.shibe.meowshiba.com)__  
This script is designed __specifically for Kindle Chinese language system__.  
__Special Note: remember to copy and paste the exported files elsewhere to avoid overrides.__  

![Example: Organized csv Notes in Notion](https://shibe.meowshiba.com/wp-content/uploads/2022/05/kindle_mac_14_notion-csv-preview-1.png "Example: Organized csv Notes in Notion")  


---

### Get All Your Highlights:

1. Clone this repository.

![Clone Repo](https://shibe.meowshiba.com/wp-content/uploads/2022/05/kindle_mac_01_clone.png "Clone Repo")  

2. Paste your `My Clippings.txt` file in it.  

![Copy My_Clippings.txt](https://shibe.meowshiba.com/wp-content/uploads/2022/05/kindle_mac_02_move-clippings-to-folder.png "Copy My_Clippings.txt")

#### In txt format:
1. For PC users, run `python .\kindle_scraper.py importAsTxt`
2. For Mac users, run `python3 kindle_scraper.py importAsTxt`
3. This script makes a folder `/highlights` in your working directory. And your highlights, companied by the locations information, are in text files named after the book's title saved in the same folder.
#### In csv format:
1. For PC users, run `python .\kindle_scraper.py importAsCsv`
2. For Mac users, run `python3 kindle_scraper.py importAsCsv`.
3. This script makes a folder `/highlights` in your working directory. Your highlights, companied by the locations information, are in csv files named after the book's title saved in the same folder.
4. Make sure to read the instructions printed on terminal to open csv files in `UTF-8 format`.

### Get List Of Titles:

1. Clone this repository. Paste your `My Clippings.txt` file in it.
2. For PC users, run `python .\kindle_scraper.py showTitles`
3. For Mac users, run `python3 kindle_scraper.py showTitles`
4. Your titles are printed on terminal.

### Get Help:

1. Clone this repository.
2. For PC users, run `python .\kindle_scraper.py help`; for Mac users, run `python3 kindle_scraper.py help`.
3. It will tell you what it can do for you.

#### References
The important reference for this tool is:
> [kindler by sanjamaniam](https://github.com/sanjaymaniam/kindler) This kindler script is used as the foundation for this scraper.
> The revisions include:
1. Encoded UTF-8 and alter parsing details to comply specifically with Kindle Chinese language system.
2. Added Kindle Location information correspondent with the highlights.
3. Added function to parse titles to comply with .txt naming conventions.
4. Added function to export .csv files for __Notion__ users.
5. Removed the JSON related functions.
6. Fixed the command line error in the terminal - _Latest Update on Aug, 2021_

#### Collaboration
The program is developed by myself. 
However, Meow involved heavily during the testing phase. 
She also contributed a lot to the documentations and this instruction.

---

To-do List:
1. Optimize the parseDetails() to include separation among `标注、笔记、书签`.
2. Include support for English system.

__Special thanks to Mimi for all the support!__  
_如果您对北美hiking感兴趣，请访问我们的网站[猫和柴的野游](https://www.meowshiba.com)_
