# -*- coding: utf-8 -*-
"""Linear regression model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DiCjRtliBM-Qge1J8Xiw_Lpxm45SGAND
"""
# calculate the accuracy, if the actual value smaller than predict value then use actual value / predict value
#  if the predict value is smaller than actual value then use predict value / actual value
#  finally, calculate the average of the accuracy
def accuracy_lr(predict,test):
    total = 0
    for i in range(len(predict)):
        if abs(test[i]) <= abs(predict[i]):
           a = abs(test[i]) / abs(predict[i])
        else:
            a =  abs(predict[i]) / abs(test[i]) 
        total += a
    accuracy = total / len(predict)
    return accuracy        
# use Linear regression to train and predict passenger flow 
# get label and training data
label = data_lough["Total"].astype(np.float64)
data = data_lough.drop('Total',1)
#  split the datasets into 80% training and 20%testing
X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.2,random_state = 0)
# ------------------------------------------------------------------------------
# Training linear regression model
model2 = linear_model.LinearRegression()
model2.fit (X_train,y_train)
predict = model2.predict(X_test)
d = accuracy_lr(y_test.reset_index(drop=True),predict)
print("Athenry Road: Linear refression accuracy is ",d)
final_data = X_test.copy()
final_data["Predict"] = predict
final_data["Actual"] = y_test
final_data["Date"] = DataFrame(pd.to_datetime(X_test["Day"]))
# -------------------------------------------------------------------------------
#  Ploting the the result, yellow points are actual value, blue points are predict value, red line is the best linear line.
x = final_data["Date"]
y = final_data["Predict"]
y1=final_data["Actual"]
plt.title("predict value vs actual value")
plt.plot(x, y,'.', label = 'predict value')
plt.plot(x, y1,'.',label = 'acutal data')
plt.plot(x, y, linewidth = '0.1', label = "best line", color='red', linestyle=':')
plt.plot(x, y, '-',color = 'grey', label  = 'best line')
plt.legend(loc = 2)
