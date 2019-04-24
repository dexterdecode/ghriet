#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:47:19 2019

@author: sunny
"""

import matplotlib.pyplot as plt  
import numpy as np  
from sklearn.cluster import KMeans 

X = np.array([[0.1, 0.6], [0.15, 0.71], [0.08, 0.9], [0.16, 0.85], [0.2, 0.3], [0.25, 0.5], [0.24, 0.1], [0.3, 0.2]])
plt.scatter(X[:,0],X[:,1], label='True Position')  

M = np.array([[0.1, 0.6],
              [0.3, 0.2]], np.float)
kmeans = KMeans(n_clusters=2, init=M, n_init=1)  
kmeans.fit(X)   

plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')  
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black') 
plt.title("Intial centroids :")
plt.show()
print("The initial centroids are",kmeans.cluster_centers_) 

kmeans = KMeans(n_clusters=2, random_state=None)
kmeans.fit(X)
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')  
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black') 
plt.title("Final centroids :")
plt.show()
print("The final centroids are",kmeans.cluster_centers_) 

