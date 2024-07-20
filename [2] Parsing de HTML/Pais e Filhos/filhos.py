from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# Filhos
for child in bs.find('table', {'id':'giftList'}).children:
    print(child)

# Irmãos
for siblings in bs.find('table', {'id':'giftList'}).tr.next_sibling:
    print(siblings)
