from urllib.request import urlopen
from bs4 import BeautifulSoup

# Testei com o meu site XD
html = urlopen('https://whoxer.github.io/poema/emplasto-de-braz-cubas.html')
bs = BeautifulSoup(html.read(), 'html.parser')


classList = bs.findAll('div', {'class':'article-body'})

for name in classList:
    print(name.get_text()) # Embora a impressão do texto não tenha ficado tão legal
                           # quanto eu queria que ficasse :C
