import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

list_df = pd.DataFrame(columns=['歌詞'])

for page in (range(1, 3)):
    base_url = 'https://www.uta-net.com'
    
    url = 'https://www.uta-net.com/lyricist/11509/0/' + str(page) + '/'
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'lxml')
    
    links = soup.find_all('td', class_='side td1')
    
    for link in links:
        a = base_url + (link.a.get('href'))
        print(a)

        response = requests.get(a)

        soup2 = BeautifulSoup(response.text, 'lxml')
        
        song_lyrics = soup2.find(id='kashi_area')
        song_lyric = song_lyrics.text
        print(song_lyric)
        song_lyric = song_lyric.replace('\n', '')
        time.sleep(1)
        
        tmp_se = pd.DataFrame([song_lyric], index=list_df.columns).T
        list_df = list_df.append(tmp_se)
        
print(list_df)

list_df.to_csv('list.csv', mode = 'a', encoding='cp932')