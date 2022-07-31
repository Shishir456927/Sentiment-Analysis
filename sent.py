import numpy as np
import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

df = pd.read_csv('pfizer_reddit_preprocessed.csv')
df['score'] = df['body'].apply(lambda review:sid.polarity_scores(str(review)))
df['compound']  = df['score'].apply(lambda score_dict: score_dict['compound'])
df=df.drop(['score'], axis=1)
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
df=df.drop(['body'], axis=1)
df2=df.groupby(['date']).sum()
df2.to_csv('sentiment_scores_by_date.csv')  