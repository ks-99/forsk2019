"""
Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

    Perform K-means clustering to distinguish urban drivers and rural drivers.
    Perform K-means clustering again to further distinguish speeding drivers from those who follow speed limits, in addition to the rural vs. urban division.
    Label accordingly for the 4 groups.

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv("deliveryfleet.csv")
dataset.isnull().any(0)

features=dataset.iloc[:,1:].values


plt.scatter(features[:,0],features[:,1])

from sklearn.cluster import KMeans

kmean=KMeans(n_clusters=2,init='k-means++',random_state=0)
pred_cluster=kmean.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Rural')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Urban')
plt.scatter(kmean.cluster_centers_[:, 0], kmean.cluster_centers_[:, 1], c = 'green', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('distance')
plt.ylabel('speed')
plt.legend()
plt.show()


#Perform K-means clustering again to further distinguish speeding drivers from those who follow speed limits, in addition to the rural vs. urban division.
#    Label accordingly for the 4 groups.

kmean=KMeans(n_clusters=4,init='k-means++',random_state=0)
pred_cluster=kmean.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Rural_limit')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Urban_limit')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'urban_speedy')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'brown', label = 'rural_speedy')
plt.scatter(kmean.cluster_centers_[:, 0], kmean.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('distance')
plt.ylabel('speed')
plt.legend()
plt.show()

