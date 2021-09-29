import requests
from bs4 import BeautifulSoup
from plyer import notification
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image  
import time
import ast



def parse_data(soup):
    data={}
    print(soup)
    soup=soup.split(" -")[0]
    print(soup)
    
    data["Followers"]=soup[0].split(" ")[0]
    print(data["Followers"])
    data["Following"]=soup[2]
    data['Post']=soup[4]
    print(data)
    instalog = open("instalog.txt","w+")
    instalog.write(str(data))
    instalog.close()


    return data



def scrape_data(URL):
    print(URL)
    r=requests.get(URL,headers = {'User-agent': 'your bot 0.1'})

    print(r)
    # print("i got it")
    # print(URL+username+"/")
    soup=BeautifulSoup(r.text,"html.parser")

    print(soup)
    meta=soup.find("meta",property="og:description")
    print(meta)
    return parse_data(meta.attrs['content'])






window=tk.Tk()

window.title("mainScreen")
window.title("mainScreen")
window.geometry("500x500")
window.configure(bg ='white')

canvas = tk.Canvas(master=window, width = 250, height = 250)      
img = ImageTk.PhotoImage(Image.open("insta.jpg")) 
canvas.create_image(20, 20, anchor=NW, image=img)
canvas.pack()      

def makeurl():
    name=username.get("1.0","end-1c")
    url="https://www.instagram.com/"+ name+"/"
    print(name)
    print(url)
    print(type(url))
    URL=url
    data=scrape_data(URL)
    return url


username =tk.StringVar(window)

# username =tk.StringVar(window)
tk.Label(master=window,text="Enter Username",font="none 20 bold",background="green",fg="black").pack()
username=tk.Text(master=window,font="none 8",bg="silver",height=1.0)
username.pack()
tk.Button(master=window,text="Notify",command=makeurl).pack()
    
window.mainloop()








if __name__ == "__main__":
    instalog=open("instalog.txt"+"r")
    dic=instalog.read()
    if dic!='':
        data=ast.literal_eval(dic)
    notification.notify(
        title="Instagram Log"
        ,message="followers" + data["Followers"]+
    data["Following"]
    +data['Post']

    )

  




