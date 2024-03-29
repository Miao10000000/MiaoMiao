#### ***All files are run in google coolab***

# Daily passenger flow prediction in Galway
## 1.Dataset processing
#### Code is in "data process" file
This part is processing passenger flow datasets and weather datasets. First, processing two tables (passenger flow and weather). Secondly, extracting useful columns and merging two tables together. Fourthly, feature extraction, for example, “Day” is 2019-08-10, it can be extracted into “year (2019)”, “day(10)”, “month(8)”, “day of week”, “day of month”, “day of year”, “season”, etc. Finaly, meging twp tables to gether according to different day. The table is as below.
![](images/1.png)
## 2.Training five models
#### Code is in "five models" file
This part is machine learning algorithms, contains five models (KNN, SVR, Linear regression, LSTM, transfer learning). Use the dataset of Athenry road to train these five models. After that testing the prediction accuracy. Finally, choosingg the models that are suitable for predicting passenger flow in Galway. The result shows KNN and LSTM model are more suitable than other models.As below
![](images/10.png)

## 3.Feature visualization
### 1. Feature correlation analysis
#### Code is in "feature correlation analysis.py"
This part focus on analyzing features and visualizing the relationship between features. It including feature importance, feature correlation, etc. Basically, using the functions in "feature selector.py" file to analyse the relationship between features. It is really useful for feature selection, some pictured are as below.

![](images/2.png)
### 2. Dropping features
#### Code is in "dropping features.py"
This part is dropping features based on previous analysis. Then predicting the passenger flow in Galway. Finally, Caluculate the accuracy and visualizing the predicted accuracy. There are five models in this part, they are KNN, LSTM, SVR, Linear regression, transfer learning. However, I only write code for three models (KNN, SVR, Linear regression). Beacuse I manually dropping features in LSTM and transfer learning models.

![](images/3.png)
## 3.Improve accuracy
#### Code is in "Improve accuracy" file
### 1. Ensemble learning
#### Code is in "ensemble_learning.py" 
This part is combining two models (KNN and LSTM) together, calculating accuracy and plot the predicted value and actual value.

![](images/5.png)

### 2. Splitting datasets
#### Code is in "splitting_dataset_into_weekday_and_weekend.py" 
This part is splitting datasets into weekday and weekend, using KNN model to predicting the passenger flow on weekday and LSTM model to predict passenger flow on weekend.

![](images/4.png)

## Datasets
All the datasets in this work are in "datasets" file. 

"Raw passenger flow datasets" contains the passenger flow of four roads. 

"Raw weather dataset" is the original weather dataset.  

"Pre-processed weather dataset" contains a pre-processed weather dataset that useful columns are extracted.

"Final dataset" contains four final datasets of four roads after feature extraction.

"Dropping features datasets" containing the datasets of five models of dropping each features.

"Accuracy comparison" is the datasets that comparing dropping features

## References
[1]. KNN: https://www.cnblogs.com/tszr/p/10794788.html

[2]. Linear regression: https://blog.csdn.net/weixin_39175124/article/details/79465558

[3]. LSTM: https://blog.csdn.net/qq_29296685/article/details/83793678

[4]. LSTM: http://blog.itpub.net/31509949/viewspace-2213894/

[5]. SVR: https://www.cnblogs.com/Lin-Yi/p/8971845.html

[6]. Transfer learning: https://blog.csdn.net/u011437229/article/details/53465086

[7]. feature selector: https://github.com/WillKoehrsen/feature-selector/tree/master/feature_selector

[8]. feature selector: https://zhuanlan.zhihu.com/p/49479702

