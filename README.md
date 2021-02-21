## Kindle Scraper for Mandarin System
Free your highlights and locations information from Kindle's `My Clippings.txt`.
This script is designed specifically for Kindle Chinese language system.
Hope you find it useful!
_Special Note: make sure to copy the exported .txt and .csv elsewhere to avoid being overwritten next time._

### Get Help:

Clone this repository.
Run `python .\kindle_scraper.py` help.
It will tell you what it can do for you.

### Get All Your Highlights:

Clone this repository. Paste your `My Clippings.txt` file in it.
#### In txt format
Run `python .\kindle_scraper.py importAsTxt`.
Your highlights, companied by the locations information, are in text files named after the book's title saved in the same folder.
#### In csv format:
Run `python .\kindle_scraper.py importAsCsv`.
Your highlights, companied by the locations information, are in csv files named after the book's title saved in the same folder.
Make sure to read the instructions printed on terminal to open csv files in `UTF-8 format`.


### Get List Of Titles:

Clone this repository. Paste your `My Clippings.txt` file in it.
Run `python kindle_scraper showTitles`.
Your titles are printed on terminal.

#### References
The important reference for this tool is:
* [kindler by sanjamaniam](https://github.com/sanjaymaniam/kindler) This kindler script is used as the foundation for this scraper.
The revisions include:
1. Encode UTF-8 and alter parsing details to comply specifically with Kindle Chinese language system.
2. Add function to parse titles to comply .txt naming conventions.
3. Add function to export .csv files for Notion users.

_Special thanks for Cat._ 