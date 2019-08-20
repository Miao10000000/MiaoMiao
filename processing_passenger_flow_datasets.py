# -*- coding: utf-8 -*-
"""Processing passenger flow datasets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DiCjRtliBM-Qge1J8Xiw_Lpxm45SGAND
"""

# 1) This part is organizing tables, convert HTML file to CSV. 
# 2) Calculating total number of passenger flow and extracting useful information from HTML
# 3) Saving passeger flow informtion of into a final table




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
from sklearn.metrics import confusion_matrix
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
from google.colab import drive
drive.mount('/content/drive')
!Is "/content/drive/My Drive/Colab Notebooks"
inputfile1 = '/content/drive/My Drive/Colab Notebooks/Athenry/201903.csv'
data1 = pd.read_csv(inputfile1, error_bad_lines=False,encoding="UTF-8")
# extract rows from 39 to 43 where is total number of passenger flow in original tables
passenger_number1 = data1[39:43]
passenger_number1 = pd.DataFrame(passenger_number1)
passenger_number1.to_csv('/content/drive/My Drive/Colab Notebooks/Athenry_result/passenger.csv', mode="a", index=False, header=True)
sign1 = data1[13:14]
# sign1 is the day
sign1_column = pd.melt(sign1)
sign1_column.to_csv('/content/drive/My Drive/Colab Notebooks/Athenry_result/totall.csv', mode="a", index=False, header=False)
label = pd.read_csv('/content/drive/My Drive/Colab Notebooks/Athenry_result/totall.csv',error_bad_lines=False,encoding = "ISO-8859-1")
columns = pd.read_csv("/content/drive/My Drive/Colab Notebooks/Athenry_result/passenger.csv",error_bad_lines=False,encoding = "ISO-8859-1")
# calculate the total number of passenger flow
total= columns.apply(lambda x:x.sum())
total = np.array(total)#np.ndarray()
total_list=total.tolist()
total_list = total_list[1:len(total_list)]
# the final table contains two columns, one is "Day" and another column is "Total"
label["Total"] = total_list
label.to_csv('/content/drive/My Drive/Colab Notebooks/Athenry_result/totall.csv', index=False, header=True)
new_table = pd.read_csv('/content/drive/My Drive/Colab Notebooks/Athenry_result/totall.csv',error_bad_lines=False,encoding = "ISO-8859-1")
new_table[0:-3].to_csv('/content/drive/My Drive/Colab Notebooks/Athenry_result/4.csv', mode="a",index=False, header=False)