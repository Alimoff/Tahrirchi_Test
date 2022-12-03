import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime
from collections import Counter

url = 'https://kun.uz/uz/news/category/jahon'
res = requests.get(url)

soup = BeautifulSoup(res.content,'html.parser')
news_= soup.find_all('a', class_='small-news__title')

info= []
for news in news_:
    link = news["href"]

    url = f'https://kun.uz{link}'
    res = requests.get(url)

    soup = BeautifulSoup(res.content,'html.parser')
    content = soup.find('div', class_='single-content').text
    time = datetime.datetime.now()
    words = content.split()

    Counter_ = Counter(words)
    most_occur = Counter_.most_common(5)


    info.append([link, time, content, words, most_occur])


columns = ["Link", "Time",  "Content", "Words", "Most occured words"]  #Columns for dataset 
df = pd.DataFrame(data=info, columns=columns)
df.to_csv('news.csv')
