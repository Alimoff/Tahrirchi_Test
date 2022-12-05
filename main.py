import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime
from collections import Counter

url = 'https://kun.uz/uz/news/category/jahon'     #We're going to parse 'jahon' news from 'Kun.uz' 
res = requests.get(url)

soup = BeautifulSoup(res.content,'html.parser')
news_= soup.find_all('a', class_='small-news__title')

info= [] # A list to gather data together

# Separate each content
for news in news_:
    link = news["href"]

    url = f'https://kun.uz{link}' # For automation URL's
    res = requests.get(url)

    soup = BeautifulSoup(res.content,'html.parser')
    content = soup.find('div', class_='single-content').text # Assigning content to a variable
    time = datetime.datetime.now() # Record the time when the parsing was done
    words = content.split()  # Separate each words

    Counter_ = Counter(words)  # Function to calculate the most repeated words
    most_occur = Counter_.most_common(5) # Sat to write the 5 most used words


    info.append([link, time, content, words, most_occur])


columns = ["Link", "Time",  "Content", "Words", "Most occured words"]  #Columns for dataset 
df = pd.DataFrame(data=info, columns=columns)
df.to_csv('news.csv') # Write to CSV file