import requests
from bs4 import BeautifulSoup
import os


URL= 'https://www.instagram.com/'
# # url="https://www.bigfootcode.ga"
# r =requests.get(url,params=payload)
# print(r.status_code)

def parse_data(soup):
    data={}
    soup=soup.split("-")[0]
    data["Followers"]=soup[0]
    data["Following"]=soup[2]
    data['Post']=soup[4]
    return data



def scrape_data(username):
    r=requests.get(URL+username+"/",headers = {'User-agent': 'your bot 0.1'})

    print(r)
    # print("i got it")
    print(URL+username+"/")
    soup=BeautifulSoup(r.text,"html.parser")

    print(soup)
    meta=soup.find("meta",property="og:description")
    print(meta)
    return parse_data(meta.attrs['content'])




if __name__=="__main__":
    username="modi"
    data=scrape_data(username)
    print(data)
    






