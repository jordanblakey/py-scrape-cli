import requests
import sys
from bs4 import BeautifulSoup


def scrape(url, soup_query):
  # Give a URL and a Beautiful Soup Query, print the response to console and
  # write to an HTML file on the Desktop.

  # EXAMPLE USAGE:
  # Takes a URL and Beautiful Soup call as arguments to scrape.py
  # python3 scrape.py "https://google.com" "find_all('a')"
  # python3 scrape.py "https://google.com" "prettify()"

  # Requires Python3 package Beautiful Soup 4
  # pip3 install beautifulsoup4

  response = requests.get(url)
  page_html = response.text
  soup = BeautifulSoup(page_html, 'html.parser')

  # Take a look at the raw HTTP Response from library 'response'
  # response
  # response.text

  # EXAMPLE SOUP_QUERIES (Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  # soup
  # soup.prettify()
  # soup.title
  # soup.title.name
  # soup.title.string
  # soup.title.parent.name
  # soup.p
  # soup.p['class']
  # soup.a
  # soup.find_all('a')
  # soup.find(id="link3")

  # for link in soup.find_all('a'):
  # print(link.get('href'))

  # #Another common task is extracting all the text from a page:
  # print(soup.get_text())

  # Print to console
  soup_query = eval('soup.' + soup_query)
  print(soup_query)

  # Write to file
  # with open('~/Desktop/soup.html', 'w') as file: file.write(str(soup_query))


scrape(sys.argv[1], sys.argv[2])
# scrape("http://google.com", "soup.find_all('a')")
