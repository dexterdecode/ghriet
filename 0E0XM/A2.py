#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:26:54 2019

@author: sunny
"""

from sklearn import tree

Age = ['<21', '<21', '21-35', '>35', '>35', '>35', '21-35', '<21', '<21', '>35', '<21', '21-35', '21-35', '>35']
Income = ['High', 'High', 'High', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'High', 'Medium']
Gender = ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Female', 'Female', 'Female', 'Male', 'Female', 'Male']
Status = ['Single', 'Married', 'Single', 'Single', 'Single', 'Married', 'Married', 'Single', 'Married', 'Single', 'Married', 'Married', 'Single', 'Married']

dataLabels = ["No","No","Yes","Yes","Yes","No","Yes","No","Yes","Yes","Yes","Yes","Yes","No"]

from sklearn import preprocessing

l = preprocessing.LabelEncoder()

age_encoded=l.fit_transform(Age)
income_encoded=l.fit_transform(Income)
gender_encoded=l.fit_transform(Gender)
status_encoded=l.fit_transform(Status)
label=l.fit_transform(dataLabels)

features=list(zip(age_encoded,income_encoded,gender_encoded,status_encoded))

trained_classifier = tree.DecisionTreeClassifier()


trained_classifier = trained_classifier.fit(features,label)


someDataOutOfTrainingSet = [[1, 1, 0, 0]]
label = trained_classifier.predict(someDataOutOfTrainingSet)

if label[0] == 1:
    print("This person buys lipstick.")
else:
    print("This person will not buy lipstick.")