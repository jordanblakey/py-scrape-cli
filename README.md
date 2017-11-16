# PyScrape CLI

Simple web scraping script to expose Beautiful Soup to the terminal.

Scrape.py takes arguments: 1) URL 2) Beautiful Soup query.
Returns HTML to the terminal & writes to scraped.html on the current directory.

Requires Python3 package Beautiful Soup 4
Installation: `pip3 install beautifulsoup4`

## Example Usage:

- `python3 scrape.py "https://google.com" "find_all('a')"`
- `python3 scrape.py "https://google.com" "prettify()"`

## Example Beautiful Soup Queries [(Soup Docs)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Note you must remove 'soup.' from your CLI arguments as shown above.

- `soup`
- `soup.prettify()`
- `soup.title`
- `soup.title.name`
- `soup.title.string`
- `soup.title.parent.name`
- `soup.p`
- `soup.p['class']`
- `soup.a`
- `soup.find_all('a')`
- `soup.find(id="link3")`
- `for link in soup.find_all('a'): print(link.get('href'))`
- `print(soup.get_text())`
