import requests
from bs4 import BeautifulSoup
url=input("enter the url where you want to scrap the data")
res=requests.get(url)
data=BeautifulSoup(res.text,'html.parser')
for text in data.find_all('p'):
   print("\n")
   print(text.string)
    

