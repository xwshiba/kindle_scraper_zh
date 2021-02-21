## Kindle Scraper for Mandarin System
Free your highlights and locations information from Kindle's `My Clippings.txt`.
This script is designed specifically for Kindle Chinese language system.
Hope you find it useful!

_Special Note: copy and paste the exported files elsewhere to avoid being overwritten next time._

### Get Help:

Clone this repository.
Run `python .\kindle_scraper.py` help.
It will tell you what it can do for you.

### Get All Your Highlights:

Clone this repository. 
Paste your `My Clippings.txt` file in it.

#### In txt format:
Run `python .\kindle_scraper.py importAsTxt`.
Your highlights, companied by the locations information, are in text files named after the book's title saved in the same folder.
#### In csv format:
Run `python .\kindle_scraper.py importAsCsv`.
Your highlights, companied by the locations information, are in csv files named after the book's title saved in the same folder.
Make sure to read the instructions printed on terminal to open csv files in `UTF-8 format`.

### Get List Of Titles:

Clone this repository. Paste your `My Clippings.txt` file in it.
Run `python .\kindle_scraper.py showTitles`.
Your titles are printed on terminal.

#### References
The important reference for this tool is:
* [kindler by sanjamaniam](https://github.com/sanjaymaniam/kindler) This kindler script is used as the foundation for this scraper.
The revisions include:
1\. Encoded UTF-8 and alter parsing details to comply specifically with Kindle Chinese language system.
2\. Added function to parse titles to comply .txt naming conventions.
3\. Added function to export .csv files for Notion users.
4\. Removed the JSON related functions.

_Special thanks to Cat for all the support_
_如果你对北美hiking感兴趣，请访问我们的网站[猫和柴的野游](https://www.meowshibatravel.com)_