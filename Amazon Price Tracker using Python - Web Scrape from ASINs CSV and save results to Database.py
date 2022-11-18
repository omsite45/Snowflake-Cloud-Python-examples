import requests
from bs4 import BeautifulSoup
import pandas as pd

url=f"https://www.flipkart.com/search?q=Canon%20EOS%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
response=requests.get(url)
response=response.content
soup= BeautifulSoup(response, 'html.parser')
(soup)
page=soup.find_all('div', class_='_2kHMtA')
#print(soup)
products=soup.find('span', class_='_4rR01T')
price = soup.find('span', class_='_30jeq3 _1_WHN1')
for p in page:
    products=p.find('div', class_='_4rR01T')
    price = p.find('div', class_='_30jeq3 _1_WHN1')
    print("Products :",products.text, "Price :" ,price.text )
