# -*- coding: utf-8 -*-
"""KNN model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DiCjRtliBM-Qge1J8Xiw_Lpxm45SGAND
"""

# Use KNN regression model to predict passenger flow
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
def accuracy_knn(predict,test):
    total = 0
    for i in range(len(predict)):
        if abs(test[i]) <= abs(predict[i]):
           a = abs(test[i]) / abs(predict[i])
        else:
            a =  abs(predict[i]) / abs(test[i]) 
        total += a
    accuracy = total / len(predict)
    return accuracy        
#  n_dots depends on different datasets
n_dots = 1625
# get label and training data
label = data_lough["Total"].astype(np.float64)
data = data_lough.drop('Total',1)
# split the dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.2,random_state = 0)


# add noise to predicting value
y_train += 0.1 * np.random.rand(n_dots) - 0.1
# set k as 4 when calculating four closet neigbhours' values
k = 4
knn = KNeighborsRegressor(k)
knn.fit(X_train,y_train)
#Calculate the fitting accuracy of the fitted curve for training samples
prec = knn.score(X_train, y_train) 
# make prediction based on testing data
y_pred = knn.predict(X_test)
r = accuracy_knn(y_pred,y_test.tolist())
print('the accuracy of Clarinbridge road in KNN model is :',r)
#  plot the predicted value and actual value
axia = [i for i in range(1,408)]
plt.plot(axia,y_test.tolist(), c='red', label='actual value')
plt.plot(axia,y_pred, c='green',label='predict value')
plt.xlabel('data')
plt.ylabel('passenger flow')
plt.title('the performace of KNN ')
plt.legend(loc = 2)
 
plt.figure()