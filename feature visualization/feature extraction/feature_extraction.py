# -*- coding: utf-8 -*-
"""Feature extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DiCjRtliBM-Qge1J8Xiw_Lpxm45SGAND
"""

# 1) This part is feature extraction, it mainly extracts features from "Day"
# 2) For example, "Day" is "2018-06-10", then extract"Year"(2018), "Month"(6), "Day of the month"(10).Extracting features according to Irish culture
# 3) The features are ['Day',	'dayofmonth'	,'dayofweek',	'week'	,'month'	,'year'	,'season',	'dayofyear',	'Easter',	'Christmas',	'Summer/winter_holiday'	,'Halloween'	,'Patrick']
# 4) The functions are used to extract features as below.
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_validate
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoCV
from sklearn.linear_model import Lasso
from sklearn import metrics
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential


# extract "Patrick" from "Day", searched the day of Patrick, then use this method to change the lable.
# If it is "Patrick" then label is "1", or the label is "0"
def function_Patrick(x):
  f = [17,18]
  if x["dayofmonth"] in f and x["month"] ==3: 
                     return 1
  else:
       return 0
    
# extract "Easter" from "Day", searched the day of Easter, then use this method to change the lable.
# If it is "Easter" then label is "1", or the label is "0"
def function_Easter(x):
  v = [21,22,23,24,25,26,27,28,29,30]
  if x["dayofmonth"]in v and x["month"] ==4:
                    return 1
  else:
       return 0
# extract "Halloween" from "Day", searched the day of Halloween, then use this method to change the lable.
# If it is "Halloween" then label is "1", or the label is "0"   
def function_Halloween(x):
  if x["dayofmonth"]==31 and x["month"] ==10:
                    return 1
  else:
       return 0
# extract "Christams" from "Day", searched the day of Christams, then use this method to change the lable.
# If it is "Christams" then label is "1", or the label is "0"      
def function_Christams(x):
  v = [25,26,27,28,29,30]
  g = [1,2,3,4,5]
  if x["dayofmonth"]in v and x["month"] ==12:
                    return 1
                    
  else: 
      if x["dayofmonth"]in g and x["month"] ==1:
                        return 1                
      else:
          return 0 
# extract "Summer_winter holiday" from "Day", searched the day of Summer_winter holiday, then use this method to change the lable.
# If it is "Summer_winter holiday" then label is "1", or the label is "0"      
def function_Summer_winter(x):
  v = [6,7,8]
  h = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
  j = [20,21,22,23,24,25,26,27,28,29,30,31]
  if x["month"] in v:
                    return 1
  else:
       if x["dayofmonth"] in v and x["month"]==1:
                         return 1
       else: 
            if x["dayofmonth"]in j and x["month"]==12:
                              return 1
            else:
                 return 0
# process the dataset, convert them into "float64"
data_lough['Day']=DataFrame(pd.to_datetime(data_lough['Day']))
data_lough['dayofmonth']=data_lough['Day'].dt.day.astype(np.float64)
data_lough['dayofweek']=data_lough['Day'].dt.dayofweek.astype(np.float64)
data_lough['week']=data_lough['Day'].dt.week.astype(np.float64)
data_lough['month']=data_lough['Day'].dt.month.astype(np.float64)
data_lough['year']=data_lough['Day'].dt.year.values.astype(np.float64)
data_lough['season']=data_lough['Day'].dt.quarter.astype(np.float64)
data_lough['dayofyear']=data_lough['Day'].dt.dayofyear.astype(np.float64)
data_lough['Day']=data_lough['Day'].astype(np.int64)
data_lough['Easter'] = data_lough.apply(lambda x: function_Easter(x), axis = 1)
data_lough['Christmas'] = data_lough.apply(lambda x: function_Christams(x), axis = 1)
data_lough['Summer/winter_holiday'] = data_lough.apply(lambda x: function_Summer_winter(x), axis = 1)
data_lough['Halloween'] = data_lough.apply(lambda x: function_Halloween(x), axis = 1)
data_lough['Patrick'] = data_lough.apply(lambda x: function_Patrick(x), axis = 1)
data_lough['Total'] = data_lough['Total'].astype(np.float64)