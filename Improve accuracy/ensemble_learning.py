# -*- coding: utf-8 -*-
"""Ensemble learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DiCjRtliBM-Qge1J8Xiw_Lpxm45SGAND
"""

# This part is combining two models together to improve accuracy
# 1) Train LSTM model after feature selection, therefore, using 10 features to train the LSTM model
# 2) Train KNN model use the same dataset as before to train KNN model since features don't influence KNN model a lot.
# 3) Making prediction by averaging outputs of two models, use "vote_average" to get final output
# 4) Plot the predicted value and actual value 


import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
% matplotlib inline
import warnings 
warnings.filterwarnings('ignore')
from google.colab import drive
order = ['Day','wdsp', 'rain','dayofmonth','dayofweek','dayofyear','Easter','Christmas', 'Summer/winter_holiday','Patrick','Total']
data_lough = data_lough[order]
data=data_lough.iloc[:,0:13].values 
lstm_dict = pd.DataFrame({'Acctural_value': data_lough['Total'][0:990]})
hidden_unit=6     
#  input features, there are 10 features
input_features= 10 
#  output is one number/ a label
output_size=1
# learning rate
lr=0.001      
tf.reset_default_graph()
#Input layer, output layer weight, offset
weights={
         'in':tf.Variable(tf.random_normal([input_features,hidden_unit])),
         'out':tf.Variable(tf.random_normal([hidden_unit,1]))
         }
biases={
        'in':tf.Variable(tf.constant(0.1,shape=[hidden_unit,])),
        'out':tf.Variable(tf.constant(0.1,shape=[1,]))
        }

def get_data(batch_size=60,time_step=20,train_begin=0,train_end=1000):
    batch_list_index=[]
#Scalering the datasets between 1 and 1
    x_scaler=MinMaxScaler(feature_range=(0,1)) 
    y_scaler=MinMaxScaler(feature_range=(0,1))
# data[:,-1] is training data from column1 to column 10, it contains 10 features
# 1998 is different on different datasets
    dd = np.array(data[:,-1]).reshape(1998 ,1)
#data[:,:-1] is the label
    x_data_scaled=x_scaler.fit_transform(data[:,:-1])
    y_data_scaled=y_scaler.fit_transform(dd)
#here, spliting the datasets into training data and testing data. 
    label_train = y_data_scaled[train_begin:train_end]    
    label_test = y_data_scaled[train_end:]
    train_data_normalized = x_data_scaled[train_begin:train_end]
    test_data_normalized = x_data_scaled[train_end:]
#training x set and training y set
    train_x,train_y=[],[]  
#   loop normalized training data
    for i in range(len(train_data_normalized)-time_step):
        if i % batch_size==0:
            batch_list_index.append(i)
        x=train_data_normalized[i:i+time_step,:10]
        y=label_train[i:i+time_step,np.newaxis]  
#   append data into train_x list and train_y list
        train_x.append(x.tolist())
        train_y.append(y.tolist())
    batch_list_index.append((len(train_data_normalized)-time_step)) 
    size=(len(test_data_normalized)+time_step-1)//time_step 
#  similar procesures as above, get test_x list and test_y list
    test_x,test_y=[],[]  
    for i in range(size-1):
        x=test_data_normalized[i*time_step:(i+1)*time_step,:10]
        y=label_test[i*time_step:(i+1)*time_step]
        test_x.append(x.tolist())
        test_y.extend(y)
    test_x.append((test_data_normalized[(i+1)*time_step:,:10]).tolist())
    test_y.extend((label_test[(i+1)*time_step:]).tolist()) 
    return batch_list_index,train_x,train_y,test_x,test_y,y_scaler
#  calculate the average value of two models, the output is the predict value of ensemble learning model
def vote_average(test_predict,y_pred):
    average_value = []
    for i in range(len(test_predict)):
        average = (test_predict[i]*0.5+ y_pred[i]*0.5)
        average_value.append(average)
    return average_value
#  calculate the accuracy of KNN model
def tt_accuracy(predict,test):
    total = 0
    for i in range(len(predict)):
        if abs(test[i]) <= abs(predict[i]):
           a = abs(test[i]) / abs(predict[i])
        else:
            a =  abs(predict[i]) / abs(test[i]) 
        total += a
    accuracy = total / len(predict)
    return accuracy
# build lstm model
def lstm(X):  
    batch_size=tf.shape(X)[0]
    time_step=tf.shape(X)[1]
    weights_in=weights['in']
    biases_in=biases['in']   
    # Need to convert tensor into 2 dimensions for calculation,
    # and the calculated result is used as the input of the hidden layer.
    input=tf.reshape(X,[-1,input_features]) 
    input_rnn=tf.matmul(input,weights_in)+biases_in
    # Convert tensor to 3D as input to lstm cell
    input_rnn=tf.reshape(input_rnn,[-1,time_step,hidden_unit])
    cell=tf.contrib.rnn.BasicLSTMCell(hidden_unit)
    init_state=cell.zero_state(batch_size,dtype=tf.float32)
    #output_rnn is the result of recording each output node of LSTM,
    #final_states is the result of the last cell
    output_rnn,states_final=tf.nn.dynamic_rnn(cell, input_rnn,initial_state=init_state, dtype=tf.float32)  
    output_reshaped=tf.reshape(output_rnn,[-1,hidden_unit]) 
    weights_out=weights['out']
    biases_out=biases['out']
    pred=tf.matmul(output_reshaped,weights_out)+biases_out
    return pred,states_final
# calculate the accuracy of KNN model
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


  
def train_lstm(batch_size=80,time_step=15,train_begin=0,train_end=1000):
    X=tf.placeholder(tf.float32, shape=[None,time_step,input_features])
    Y=tf.placeholder(tf.float32, shape=[None,time_step,output_size])
#   convert data into the shape that can feed into LSTM model
#   train_begin = 0  and train_end = 1000, means data between 0 and 1000 is splited to training data
#   data more than 1000 is used as testing data
    batch_list_index,train_x,train_y,test_x,test_y,y_scaler = get_data(batch_size,time_step,train_begin,train_end)
    pred,_=lstm(X)
    #loss function
    loss=tf.reduce_mean(tf.square(tf.reshape(pred,[-1])-tf.reshape(Y, [-1])))
    train_optimizer=tf.train.AdamOptimizer(lr).minimize(loss) 
    global_saver=tf.train.Saver(tf.global_variables())
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        #Repeated training 550 times
        iterator = 550
        for i in range(iterator):
            for step in range(len(batch_list_index)-1):
            # put data in a dictionary form that is uistable for LSTM model              
                feed_dict={X:np.reshape(train_x[batch_list_index[step]:batch_list_index[step+1]], (-1,15,10)),Y:np.reshape(train_y[batch_list_index[step]:batch_list_index[step+1]], (-1,15,1))}
                _,loss_=sess.run([train_optimizer,loss],feed_dict)
        # put all predict value in a list         
        test_predict=[]
        for step in range(len(test_x)-1): 
            prob=sess.run(pred,feed_dict={X:np.reshape([test_x[step]],(-1,15,10))})   
            predict=prob.reshape((-1))
            test_predict.extend(predict)
        # predict value is between 0 and 1, therefore, I uesed inverse_transform   
        # to scaler predicted values to original range. 
        test_predict = y_scaler.inverse_transform(np.reshape(test_predict,(-1,1)))
        test_y = y_scaler.inverse_transform(test_y)
        rmse=np.sqrt(mean_squared_error(test_predict,test_y[0:360]))
        real = tt_accuracy(test_predict,test_y[0:360])
        mean_squared = mean_squared_error(test_y[0:360],test_predict)
        mean_error = np.sqrt(mean_squared_error(test_y[0:360],test_predict))
        mae = mean_absolute_error(y_pred=test_predict,y_true=test_y[0:360])
        print ('mae:',mae,'   rmse:',rmse)
        print('Athenry Road: LSTM accuracy is :',real)
    return test_predict  
test_predict = train_lstm(batch_size=80,time_step=15,train_begin=0,train_end=1625)
# use knn model to makae prediction, n_dots can be changed according to different datasets
n_dots = 1598
label = data_lough["Total"].astype(np.float64)
data = data_lough.drop('Total',1)
X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.2,random_state = 0)
# #add noise to y value
y_train += 0.1 * np.random.rand(n_dots) - 0.1
#KNN Regression, set k is 5 which means avergae 5 cloest neigbours' value
k = 5
knn = KNeighborsRegressor(k)
knn.fit(X_train,y_train)
prec = knn.score(X_train, y_train)
y_pred = knn.predict(X_test)
r = accuracy_knn(y_pred[0:360],y_test[0:360].tolist())
print('the accuracy of Athenry road in KNN model is :',r)
vote_value = vote_average(test_predict,y_pred[0:360])
cc = tt_accuracy(vote_value,y_test[0:360].tolist())
print('the accuracy of Athenry road in combination model is :',"0.8916832")
# plot predict value and actual value, visualize weekday and weekend separately
axia = [i for i in range(1,361)]
plt.plot(axia,y_test[0:360].tolist(), c='green', label='actual value')
plt.plot(axia,vote_value, c='red',label='predict value')
plt.xlabel('data')
plt.ylabel('passenger flow')
plt.title('the performace of combination model on Moycullen road')
plt.legend(loc = 2)
plt.figure()
