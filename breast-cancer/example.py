import numpy as np 
import sklearn as sk 
from sklearn.model_selection import train_test_split # sklearn utility to split dataset into to sets
from sklearn.metrics import classification_report # sklearn utility to evaluate model preformance 
from sklearn.datasets import load_breast_cancer # dataset built into sklearn
from sklearn.linear_model import LinearRegression # linear regression
from sklearn.svm import SVC # support vector classification -- https://en.wikipedia.org/wiki/Support_vector_machine
from sklearn.ensemble import RandomForestClassifier # ensemble learning technique -- https://en.wikipedia.org/wiki/Random_forest

dataset = load_breast_cancer()
# datset contains:
# data: numpy array of features
# target: label of 0 or 1 for malignent of benign
# target_names: names (malignent and benign)
# DESCR: Description of dataset -- dataset has 569 subjects 
# feature_names: names of each of the features of the data (mean area, compactness, concavity, texture, smoothness)
# filename: path to dataset csv

print(dataset["data"].shape)
print(dataset["target"].shape)
for key, value in dataset.items():
    print(key)

# classifier -- switch which one is commented out to switch models
clf = SVC() # okay for this problem
# clf = LinearRegression() # worst for this problem -- never guesses class 0
# clf = RandomForestClassifier( # best classifier of the three
#     n_estimators=50, # number of "weak trees" guessing
#     n_jobs = -1 # number of CPUs to use -- -1 means use all available
#     )

X = dataset["data"]
y = dataset["target"]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # split the dataset into training and testing

clf.fit(x_train, y_train) # train the model on 70% of the dataset

print("Raw Accuracy: ", clf.score(x_test, y_test)) # clf.score gives you the accuracy of your model

y_prediction = clf.predict(x_test) # the predict method give you the model prediction for the inputs

y_prediction = np.rint(y_prediction) # round outputs to be nearest integer (0 or 1)

print(classification_report(y_test, y_prediction)) # classification_report gives more meaningful model evaluation scores


