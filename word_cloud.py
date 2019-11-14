from wordcloud import WordCloud

with open('wakati_list.txt', encoding='utf-8') as text_file:
    f = text_file.read()
    
    fpath = 'C:/Windows/Fonts/YuGothM.ttc'
    
    stop_words = ['それ', 'そう', 'ない', 'いる', 'する', 'まま', 'よう', 'てる', 'なる', 'こと', 'もう', 'いい', 'ある', 'ゆく', 'れる']
    
    wordcloud = WordCloud(background_color='white',
                          font_path=fpath, width=800, height=600, stopwords=set(stop_words)).generate(f)
    
    wordcloud.to_file('./wordcloud.png')