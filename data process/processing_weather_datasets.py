# -*- coding: utf-8 -*-
"""Processing weather datasets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DiCjRtliBM-Qge1J8Xiw_Lpxm45SGAND
"""

#process weather datasets, it including:
#1) Extracting useful information from original datasets
#2) Selecting meaningful columns as useful features
#3) Filtering out outliers
#4) Visualizing comparison before and after filtering abnormal values

from sklearn.metrics import confusion_matrix
from pandas import Series,DataFrame
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
from google.colab import drive
drive.mount('/content/drive')
!Is "/content/drive/My Drive/Colab Notebooks"
# passenger flow table
inputfile1 = '/content/drive/My Drive/Colab Notebooks/Athenry_result/final_table.csv'
data_lough = pd.read_csv(inputfile1, encoding="UTF-8")
# weather table which contains "rain", "temperature", "wind speed" and so forth
inputfile2 = '/content/drive/My Drive/Colab Notebooks/dly1875.csv'
weather = pd.read_csv(inputfile2, encoding="UTF-8")
table = pd.merge(data_lough,weather,on='Day')  
# -----------------------------------------------------------------------

# this is use mean +/- 2*standard diviation to filter out outliers
# plot destribution of before filtering and after filtering
import matplotlib.pyplot as plt
value =  data_lough["Total"]
mean = value.mean()
std = value.std()
def normfun(x,mu, sigma):
    pdf = np.exp(-((x - mu)**2) / (2* sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf
x = np.arange(0, 80000,100)
# Probability density corresponding to x number
y = normfun(x, mean, std)
plt.title("Raw data distribution")
# Parameter, color, line width
plt.plot(x,y, color='g',linewidth = 3)
# Data, array, color, color shade, group width, display frequency
plt.hist(value, bins =7, color = 'r',alpha=0.5,rwidth= 0.9, normed=True)
plt.show()
# ----------------------------------------------------------------------
# this place is to filter out mean+/-2*SD
filter_sd =data_lough["Total"].apply(lambda x: np.NaN if x < mean - 2*std or x > mean + 2*std else x)
# creat a new dataFrame, which has 7 columns. They are 'Day', 'Total',"maxtp","mintp","rain","cbl","wdsp"
dataset1 = table.loc[0:len(table["Day"]), ['Day', 'Total',"maxtp","mintp","rain","cbl","wdsp"]]
Day = dataset1["Day"].apply(lambda x: np.NaN if str(x).isspace() else x)
maxtp = dataset1["maxtp"].apply(lambda x: np.NaN if str(x).isspace() else x)
mintp = dataset1["mintp"].apply(lambda x: np.NaN if str(x).isspace() else x)
rain = dataset1["rain"].apply(lambda x: np.NaN if str(x).isspace() else x)
cbl = dataset1["cbl"].apply(lambda x: np.NaN if str(x).isspace() else x)
wdsp = dataset1["wdsp"].apply(lambda x: np.NaN if str(x).isspace() else x)
dataset = DataFrame({"Day":Day,"Total":filter_sd,'maxtp' : maxtp,'mintp' : mintp,'rain' : rain , 'cbl' : cbl, 'wdsp' : wdsp})

# convert "Day" into date type, other columns are converted into numberic 
data_lough["Day"] = DataFrame(pd.to_datetime(dataset["Day"]))
data_lough["Total"] = DataFrame(pd.to_numeric(dataset["Total"]))
data_lough["maxtp"] = DataFrame(pd.to_numeric(dataset["maxtp"]))
data_lough["mintp"] = DataFrame(pd.to_numeric(dataset["mintp"]))
data_lough["wdsp"] = DataFrame(pd.to_numeric(dataset["wdsp"]))
data_lough["rain"] = DataFrame(pd.to_numeric(pd.to_numeric(dataset["rain"], errors='coerce').fillna(0).astype(int)))
data_lough["cbl"] = DataFrame(pd.to_numeric(pd.to_numeric(dataset["cbl"], errors='coerce').fillna(0).astype(int)))
data_lough = data_lough.dropna()

# -----------------------------------------------------------------------
# plot destribution

value1 =  data_lough["Total"]
mean1 = value1.mean()
std1 = value1.std()
xx = np.arange(0, 80000,100)
yy = normfun(xx, mean1, std1)
plt.title("Data distribution without outlier")
plt.plot(xx,yy, color='g',linewidth = 3)
plt.hist(value1, bins =7, color = 'r',alpha=0.5,rwidth= 0.9, normed=True)
plt.show()
