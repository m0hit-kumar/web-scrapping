import requests
from bs4 import BeautifulSoup

url= 'https://www.codewithharry.com'

r =requests.get(url)


htmlContent =r.content
# print(htmlContent)

soup= BeautifulSoup(htmlContent,'html.parser')

# print(soup.prettify)


title=soup.title.string

# print(title)

paras=soup.find('p')
print(paras.get_text())
# print(soup.find('p')['class'])

# print(paras)

# text =soup.find_all('p').get_text()
# print(text)
