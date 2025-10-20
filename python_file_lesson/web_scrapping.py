
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
       get_single_items_data(href)
    page += 1


def get_single_items_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.find_all('div', {'class' : 'i-name'}):
       print(item_name.string)



trade_spider(1)


def german_name_list(item_url):
   source_code  = requests.get(item_url)
   plain_text = source_code.text
   soup = BeautifulSoup(plain_text, "html.parser")
   for item_names in soup.find_all("a", {'class' : 'name' }):
      print(item_names.string)


german_name_list("https://listophile.com/names/nationality/german/")