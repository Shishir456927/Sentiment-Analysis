import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
import datetime
import numpy as np


# figure
df = pd.read_csv("sentiment_scores_by_date.csv")
df2 = pd.read_csv("data.csv")
df2=df2[['date','d']]

#fig, ax = plt.subplots(1, figsize=(12,4), facecolor='#293952')
#ax.set_facecolor('#293952')
# data
sentscore = df['compound']
stockprice = df2['d']

"""
# plot
plt.plot(df.date, sentscore, marker='o', markersize=4, color='#FDAC53', linewidth=2.5)
plt.plot(df2.date,stockprice, marker='o', markersize=4, color='#BBBC53', linewidth=2.5)
# ticks n title
ax.tick_params(axis='both', colors='w')
plt.xticks(df.date[::3])
plt.title('Sentiment Score vs Date\n', loc='left', color='w', fontsize=16)
# spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('w')
ax.spines['bottom'].set_color('w')
# grid
ax.set_axisbelow(True)
ax.yaxis.grid(color='#FDAC53', linestyle='dashed', alpha=0.5)
plt.xticks(rotation=90)
plt.show()
"""
df['date'] = pd.to_datetime(df['date'])
df2['date'] = pd.to_datetime(df2['date'])
ax = df.plot(x='date', y='compound', label='Sentiment Score')
df2.plot(x='date', y='d', label='Stock Price', ax=ax)

plt.show()