import pandas as pd
import re
from nltk.corpus import stopwords
import string
#from sklearn.feature_extraction.text import CountVectorizer
import random
import matplotlib.pyplot as plt
import numpy as np
import pickle
from emot.emo_unicode import UNICODE_EMOJI
import emoji

def remove_URL(text):
    url = re.compile(r"https?://\S+|www\.\S+")
    #"(?:\@|http?\://|https?\://|www)\S+"
    #url = re.compile(r"(?:\@|http?\://|https?\://|www)\S+")
    text= url.sub(r"", text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub("$[A-Za-z0-9_]+","", text)
    text = re.sub("[0-9]+","", text)
    text=text.replace("#"," ")
    #text=text.replace("$"," ")
    return text

def convert_emojis_to_word(text):
    text=str(text)
    text = emoji.demojize(text)
    text = text.replace(":"," ")
    text = ' '.join(text.split())
    return text

def remove_punct(text):
    text=text.replace("_"," ")
    text=text.replace(","," ")
    text=text.replace("  "," ")
    table = str.maketrans("", "", string.punctuation)
    return text.translate(table)

def remove_nonascii(new_str):
    new_val = new_str.encode("ascii", "ignore")
    updated_str = new_val.decode()
    return updated_str

stop = set(stopwords.words("english"))
def remove_stopwords(text):
    #text=text.replace("confusion","")
    text = [word.lower() for word in text.split() if word.lower() not in stop]
    
    return " ".join(text)

data=pd.read_csv('reddit_pfizer_vaccine.csv')#,encoding='UTF-8')#https://www.w3schools.com/charsets/ref_html_8859.asp
#data=data[1:10]
data=data[['timestamp','body','score']]
data['timestamp'] = pd.to_datetime(data['timestamp'])
data['date'] = data['timestamp'].dt.date
data=data.drop(['timestamp'], axis=1)
data=data.dropna()

#print(data['text'])
data["body"] = data.body.map(lambda x: convert_emojis_to_word(x))

data["body"] = data.body.map(lambda x: remove_nonascii(x))
data["body"] = data.body.map(lambda x: remove_URL(x))#remove urls, hashtags and mentions-> @user

data["body"] = data.body.map(lambda x: remove_punct(x))
data["body"] = data["body"].map(remove_stopwords)#remove stopewords like the,is,of... and convert to lowercase

data=data.sort_values("date")
print(data.head(),"\n\n",data.tail())

data.to_csv('pfizer_reddit_preprocessed.csv')