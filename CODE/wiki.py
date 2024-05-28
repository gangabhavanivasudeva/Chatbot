import requests
from bs4 import BeautifulSoup
x = requests.get("https://google.com/search?q=Mahadev")
y = BeautifulSoup(x.content, 'html5lib')

# sr = y.select('.r a')
f = open('output.txt', 'w')
f.write(y.prettify())
f.close()
# print(y)