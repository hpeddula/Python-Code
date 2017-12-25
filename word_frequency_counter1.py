import requests
from bs4 import BeautifulSoup

def start(url):
    word_list=[]
    source_code=requests.get(url).text
    soup=BeautifulSoup(source_code)
    for post_text in soup.findAll('a',{'class':'index_singleListingTitles'}):
        content=post_text.string
        words=content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_list=[]
    for word in word_list:
        symbol='!@#$%^&*()\"\':'
            for i in range(0,len(symbol)):
                word =word.replace(symbol[i],"")
            if len(word) > 0:
                clean_list.appen(word)
                

