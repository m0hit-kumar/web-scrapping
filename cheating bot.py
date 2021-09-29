
import requests
from bs4 import BeautifulSoup
import os
# from google import search

url="https://erp.mmumullana.org/student/quiz/start"

# url="https://web.whatsapp.com/"




r =requests.get(url)

with open("sitee.html", "wb") as file:
    file.write(r.content)



# htmlContent =r.content
# # print(htmlContent)


# soup= BeautifulSoup(htmlContent,'html.parser')

# with open('mmdu.html,"wb') as f:
#     f.write(soup)
