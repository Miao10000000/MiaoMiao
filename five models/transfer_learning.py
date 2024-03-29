# -*- coding: utf-8 -*-
"""Transfer learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DiCjRtliBM-Qge1J8Xiw_Lpxm45SGAND
"""
# reference: https://blog.csdn.net/u011437229/article/details/53465086
# Use transfer learning model from tensorflow to make prediction since my limited datasets
# 1) Build model by myself
# 2) Write "get_train_test_data" to get training and testing dataset
# 3) Use "get_normalization_data" to get normalized datasets
# 4) Call "build_model" to buid transfer learning model
# 5) Fit the model by using "normalizaed_train_data" and "normalizaed_train_labels"
# 6) Calculate accuracy by call "tt_accuracy" function
# 7) Plot the predicted vale and actual value
 
import pathlib
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import seaborn as sns

# get data, spliting into 80% training and 20% testing data
def get_train_test_data(transfer_learning_data):
    label = transfer_learning_data['Total']
    dataset = transfer_learning_data.drop('Total',1)
    X_train_transfer, X_test_transfer, y_train_transfer, y_test_transfer = train_test_split(data, label, test_size=0.2,random_state = 0)
    return X_train_transfer, X_test_transfer, y_train_transfer, y_test_transfer
# normalized data    
def get_normalization_data(data):
    normal_data = data
    training_data = normal_data.describe()
    training_data_flit = training_data.transpose()
    normalized_data = (normal_data - training_data_flit['mean']) / training_data_flit['std']
    return normalized_data
  
# build transfer learning model   
def build_model():
  X_train_transfer, X_test_transfer, y_train_transfer, y_test_transfer = get_train_test_data(data_lough)
  model = keras.Sequential([
    layers.Dense(10, activation=tf.nn.relu, input_shape=[len(X_train_transfer.keys())]),
    layers.Dense(10, activation=tf.nn.relu),
    layers.Dense(1)
  ])
  
  optimizer = tf.keras.optimizers.RMSprop(0.001)
# calculate the mean squared error
  model.compile(loss='mean_squared_error',
                optimizer=optimizer,
                metrics=['mean_absolute_error', 'mean_squared_error'])
  return model
model = build_model()
model.summary()
# just plot the points to prompt the model is in progress 
class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

EPOCHS = 1
# split the dataset by calling the "get_train_test_data", 80% trainin and 20% testing dataset
X_train_transfer, X_test_transfer, y_train_transfer, y_test_transfer = get_train_test_data(data_lough)
# nomalize the data by calling "get_normalization_data"
normalizaed_train_data = get_normalization_data(X_train_transfer)
normalizaed_train_labels = get_normalization_data(y_train_transfer)
normalizaed_test_data = get_normalization_data(X_test_transfer)
normalizaed_test_labels = get_normalization_data(y_test_transfer)

# fit the model by using "normalizaed_train_data" and "normalizaed_train_labels"
history = model.fit(
  normalizaed_train_data, normalizaed_train_labels,
  epochs=EPOCHS, validation_split = 0.2, verbose=0,
  callbacks=[PrintDot()])


hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()
# calculate the accuracy, if the actual value smaller than predict value then use actual value / predict value
#  if the predict value is smaller than actual value then use predict value / actual value
#  finally, calculate the average of the accuracy
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

#  use transfer learning to make prediction
test_predictions = model.predict(normalizaed_test_data).flatten()
#  call tt_accuracy to calculate the accuracy, 
dd = tt_accuracy(test_predictions,normalizaed_test_labels.tolist())
print('accuracy is:',dd)
s = mean_squared_error(normalizaed_test_labels.tolist(),test_predictions)#mse
d = np.sqrt(mean_squared_error(normalizaed_test_labels.tolist(),test_predictions))
print('Ayhenry road: mean squared error of transfer learning is  :',d)
plt.figure(figsize=(24,8))
plt.plot(normalizaed_test_labels.tolist())
plt.plot([None for _ in range(0)] + [x for x in test_predictions])
plt.show()
dd = tt_accuracy(test_predictions,list(normalizaed_test_labels))
print('accuracy is:',dd)
