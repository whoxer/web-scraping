from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as err:
        print(err)
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as err:
        print(err)
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')

if title == None:
    print('Título não foi encontrado.')
else:
    print(title)
