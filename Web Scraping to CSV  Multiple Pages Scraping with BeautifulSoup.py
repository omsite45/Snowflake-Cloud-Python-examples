import requests
from bs4 import BeautifulSoup
import pandas as pd
for i in range(1,51):
    url=f"https://books.toscrape.com/catalogue/category/books_1/page-{i}.html"
    response=requests.get(url)
    response=response.content
    soup= BeautifulSoup(response, 'html.parser')
    (soup)
    ol=soup.find('ol')
    articles=ol.find_all('article',class_='product_pod')
    books=[]
    for article in articles:
      image= article.find('img')
      title=image.attrs['alt']
      rating = article.find('p')
      price=article.find('p', class_='price_color').text 
      star=rating['class'][1]
      print("title is :", title)
      print("Rating is    :",  star )
      print("Price  in £ is  : ", price[1:])
      books.append(['title', 'price', 'star'])
      df=pd.DataFrame(books, columns=['title', 'price', 'star'])
      df.to_csv('books.csv')

