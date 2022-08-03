import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
import datetime
import numpy as np

"""
df = pd.read_csv("sentiment_scores_by_date.csv")
df.plot.line(x="date",y="compound",title="Sentiment Scores vs Date")
plot.xticks(rotation=90)
plot.gcf().set_size_inches(20, 10)
plot.show(block=True)
df = pd.read_csv("sentiment_scores_by_date.csv")
x = df["date"].tolist()
y = df["compound"].tolist()
fig = plt.figure()
fig.set_figwidth(50)
fig.set_figheight(75)
ax1 = fig.add_subplot(111)
ax1.plot(np.arange(len(x)), y)
ax1.set_xticks(np.arange(len(x)/2))
ax1.set_xticklabels(x)
plt.xticks(rotation=90)
plt.show()
"""

# figure
df = pd.read_csv("sentiment_scores_by_date.csv")
fig, ax = plt.subplots(1, figsize=(12,4), facecolor='#293952')
ax.set_facecolor('#293952')
# data
price = df['compound']
# plot
plt.plot(df.date, price, marker='o', markersize=4, color='#FDAC53', linewidth=2.5)
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