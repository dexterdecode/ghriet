"""
Created on Wed Apr 10 13:31:11 2019
@author: sunny

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4, 4, 6])
y = np.array([4, 2, 6, 4])
x1 = np.array([4, 6])
y1 = np.array([4, 2])

def showplot(plot = "lemma"):
    plt.scatter(x,y,color='blue')
    plt.scatter(x1,y1,color='orange')
    plt.title("Initial Plot :")
    if plot != "lemma":
        plt.scatter([[6]],[[6]],color=plot)
        plt.title("Result Plot :")
    plt.axis([0, 10, 0, 10])
    plt.grid()
    plt.show()
showplot()
x_coordinate = [2, 4, 4, 4, 6, 6]
y_coordinate = [4, 2, 4, 6, 2, 4]

color_class = ['blue','blue','orange','blue','orange','blue']

from sklearn import preprocessing

l = preprocessing.LabelEncoder()

x_encoded=l.fit_transform(x_coordinate)
y_encoded=l.fit_transform(y_coordinate)
label=l.fit_transform(color_class)

features=list(zip(x_encoded,y_encoded))

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)

model.fit(features,label)

predicted= model.predict([[2,2]])
if predicted == 0:
    showplot("blue")
    print("The class of Co-ordinates (6,6) is Blue.")
else:
    showplot("orange")
    print("The class of Co-ordinates (6,6) is Orange.")
    
#knn = KNeighborsClassifier(metric='wminkowski', p=2, metric_params={'w': np.random.random(x_encoded.shape[0])})
#knn.fit(features,label)
#
#predicted= knn.predict([[2,2]])
#if predicted == 0:
#    showplot("blue")
#    print("The class of Co-ordinates (6,6) Using Distance weighted and Locally weighted Averaging Knn is Blue.")
#else:
#    showplot("orange")
#    print("The class of Co-ordinates (6,6) Using Distance weighted and Locally weighted Averaging Knn is Orange.")