import requests
from bs4 import BeautifulSoup
url=input("Enter the url from where you want to scrape the data : ")
res=requests.get(url)
data=BeautifulSoup(res.text,'html.parser')
head=data.title.string
body=data.find_all('p')
print(data.title.string)
for text in body:
   print("\n")
   print(text.string)


