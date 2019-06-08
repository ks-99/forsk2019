"""

Q3.Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv("data.csv")

#1. Visualize the various countries from where the artworks are coming.
a=dataset["Country"].value_counts()
plt.pie(a.values,labels=a.index,autopct='%1.1f%%')
plt.xticks(a.index,rotation=90)
plt.setp(autotexts, size=8, weight="bold")
plt.show()

#2. Visualize the top 2 classification for the artworks
a=dataset["Classification"].value_counts()
a=a.head(2)
plt.bar(a.index,a.values)


#4. Visualize the top 2 culture for the artworks
a=dataset["Culture"].value_counts()
a=a.head(2)
plt.bar(a.index,a.values)


#3.Visualize the artist interested in the artworks
"""
wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
"""
wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

