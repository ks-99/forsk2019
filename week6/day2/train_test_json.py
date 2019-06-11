"""

(Click Here To Download Training data File): 
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json

(Click Here To Download Test data File):
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json


This is the data for local classified advertisements. It has 9 prominent sections: jobs, resumes, gigs, personals, housing, community, services, for-sale and discussion forums. Each of these sections is divided into subsections called categories. For example, the services section has the following categories under it:
beauty, automotive, computer, household, etc.

For a set of sixteen different cities (such as newyork, Mumbai, etc.), we provide to you data from four sections

        for-sale
        housing
        community
        services

and we have selected a total of 16 categories from the above sections.

        activities
        appliances
        artists
        automotive
        cell-phones
        childcare
        general
        household-services
        housing
        photography
        real-estate
        shared
        temporary
        therapeutic
        video-games
        wanted-housing

Each category belongs to only 1 section.

About Data:

        city (string) : The city for which this Craigslist post was made.
        section (string) : for-sale/housing/etc.
        heading (string) : The heading of the post.

each of the fields have no more than 1000 characters. The input for the program has all the fields but category which you have to predict as the answer.

A total of approximately 20,000 records have been provided to you, proportionally represented across these sections, categories and cities. The format of training data is the same as input format but with an additional field "category", the category in which the post was made.

Task:

    Given the city, section and heading of an advertisement, can you predict the category under which it was posted?
    Also Show top 5 categories which has highest number of posts

"""

import pandas as pd

import pandas as pd

with open("data.json") as fp:
    data=fp.read()
    
data=data[data.find("{"):]

df=pd.read_json(data,lines=True)
features_train=df.iloc[:,[1,3]]

labels=df.iloc[:,0]

with open("test.json") as fp:
    data=fp.read()

data=data[data.find("{"):]
test=pd.read_json(data,lines=True)
x=pd.DataFrame(test["heading"])
test=test[["city","section"]]


from sklearn.preprocessing import LabelEncoder    
le=LabelEncoder()
features_train.iloc[:,0]=le.fit_transform(features_train.iloc[:,0])
test.iloc[:,0]=le.transform(test.iloc[:,0])

le2=LabelEncoder()
features_train.iloc[:,1]=le.fit_transform(features_train.iloc[:,1])
test.iloc[:,1]=le.transform(test.iloc[:,1])

#*******************************
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus=[]
for i in range(0, 20217):
    review = re.sub('[^a-zA-Z]', ' ', df['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()

import numpy as np
features1=np.append(features_train,features,axis=1)


corpus=[]
for i in range(0, 15370):
    review = re.sub('[^a-zA-Z]', ' ', x['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
feature2=np.append(test,features,axis=1)


le=LabelEncoder()
labels=le.fit_transform(labels)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(features1,labels)

# Predicting the Test set results
labels_pred = classifier.predict(feature2)

