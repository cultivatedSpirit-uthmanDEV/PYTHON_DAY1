"""
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
  page = 1
  while page <= max_pages:
    url = 'https://quotes.toscrape.com/page=' + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for link in soup.findAll('a' , {'class' : 'item-name'}):
       href = "https://quotes.toscrape.com/page/1/" + link.get('href')
       print(href)
    page += 1


trade_spider(1)

"""

import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://quotes.toscrape.com/page/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            print(f'"{text}" — {author}')
        
        page += 1

trade_spider(1)

