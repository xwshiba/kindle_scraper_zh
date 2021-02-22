## Kindle Scraper for Mandarin System
Free your highlights and locations information from Kindle's `My Clippings.txt`.  
This script is designed __specifically for Kindle Chinese language system__.  
Hope you find it useful!  

__Special Note: copy and paste the exported files elsewhere to avoid being overwritten.__

### Get Help:

1. Clone this repository.
2. Run `python .\kindle_scraper.py` help (Mac Users please change your command accordingly).
3. It will tell you what it can do for you.

### Get All Your Highlights:

1. Clone this repository. 
2. Paste your `My Clippings.txt` file in it.

#### In txt format:
1. For PC users, run `python .\kindle_scraper.py importAsTxt`; for Mac users, run `python3 kindle_scraper.py importAsTxt`.
2. This script makes a folder `/highlights` in your working directory. Open it.
3. Your highlights, companied by the locations information, are in text files named after the book's title saved in the same folder.
#### In csv format:
1. For PC users, run `python .\kindle_scraper.py importAsCsv`; for Mac users, run `python3 kindle_scraper.py importAsCsv`.
2. This script makes a folder `/highlights` in your working directory. Open it.
3. Your highlights, companied by the locations information, are in csv files named after the book's title saved in the same folder.
4. Make sure to read the instructions printed on terminal to open csv files in `UTF-8 format`.

### Get List Of Titles:

1. Clone this repository. Paste your `My Clippings.txt` file in it.
2. For PC users, run `python .\kindle_scraper.py showTitles`; for Mac users, run `python3 kindle_scraper.py showTitles`.
3. Your titles are printed on terminal.

#### References
The important reference for this tool is:
> [kindler by sanjamaniam](https://github.com/sanjaymaniam/kindler) This kindler script is used as the foundation for this scraper.

The revisions include:
1. Encoded UTF-8 and alter parsing details to comply specifically with Kindle Chinese language system.
2. Added function to parse titles to comply with .txt naming conventions.
3. Added function to export .csv files for __Notion__ users.
4. Removed the JSON related functions.

---

__Special thanks to Mimi for all the support!__  
_如果您对北美hiking感兴趣，请访问我们的网站[猫和柴的野游](https://www.meowshiba.com)_