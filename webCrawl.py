from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Telephone"
source_code = requests.get(url)
#All contents of the website
plain_text = source_code.text
#print(plain_text)
soup = BeautifulSoup(plain_text)
print(soup)
for heading in soup.findAll('span', {'class': 'mw-headline'}):
    title = heading.string
    print(title)