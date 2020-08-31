import requests
from bs4 import BeautifulSoup

html_doc = requests.get("https://codemy.com/")

soup = BeautifulSoup(html_doc.text,"html.parser")

coba1 = soup.findAll(attrs={"class":"info-content"})

coba2 = soup.findAll("strong")

print(len(coba1))

for i in coba1:
    print(i.find('img'))

"""
try:
    for i in all:
        print(i.find('strong'))
except:
    print()
    
    for i in coba:
    print(i.text)

for i in all:
    print(i.find('a').find('img'))
"""

