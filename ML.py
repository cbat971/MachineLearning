#General imports
import numpy as np
import pandas as pd
#ML function imports
from sklearn.model_selection import train_test_split
#preprocessing modules
from sklearn import preprocessing
#random forest models
from sklearn.ensemble import RandomForestRegressor
#cross-validation
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
#evaluation metrics
from sklearn.metrics import mean_squared_error, r2_score
#module for saving scikit-learn models
from sklearn.externals import joblib

#Chris' imports
from datetime import datetime

#load wine data from remote URL
dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')
# print(data.head())
# print(data.shape)
# print(data.describe())

y = data.quality
X = data.drop('quality', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, 
									test_size=0.2,
									random_state=123,
									stratify=y)
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
# print(X_train_scaled.mean(axis=0))
# print(X_train_scaled.std(axis=0))

X_test_scaled = scaler.transform(X_test)
# print(X_test_scaled.mean(axis=0))
# print(X_test_scaled.std(axis=0))

#Pipeline with preprocessing and model
pipeline = make_pipeline(preprocessing.StandardScaler(),
						RandomForestRegressor(n_estimators=100))

# print(pipeline.get_params())

#Declare hyperparameters to tune
hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
					'randomforestregressor__max_depth': [None, 5, 3, 1]}

#Sklearn cross-validation with pipeline
clf = GridSearchCV(pipeline, hyperparameters, cv=10)
#fit and tune model
print("Here we go")
print("This should take about 50 seconds and it started at {}:{}:{}".format(datetime.now().hour, datetime.now().minute, datetime.now().second))
clf.fit(X_train, y_train)
print("And ended at: {}:{}:{}".format(datetime.now().hour, datetime.now().minute, datetime.now().second))
# print(clf.best_params_)
# print(clf.refit)

#predict a new set of data
y_pred = clf.predict(X_test)
print(r2_score(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))


joblib.dump(clf, 'rf_regressor.pkl')

clf2 = joblib.load