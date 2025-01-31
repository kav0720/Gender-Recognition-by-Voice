# -*- coding: utf-8 -*-
"""VoiceClassification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DizIDWD1qHfkJtewS3bz-h_vtqHoP44h

**Problem statement:** Create a classification model to predict the gender (male or
female) based on different acoustic parameters
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

df=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/voice.csv')

df.head()

# dealing with null and NaN values
df.isnull().sum()

#checking for duplicates
df.duplicated()

#percentage distribution of target label
import matplotlib.pyplot as plt
df['label'].value_counts().plot(kind='pie',autopct='%1.1f%%')

from sklearn.model_selection import train_test_split
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train,X_test,y_train,y_test= train_test_split(X, y, test_size=0.2, random_state=0)

"""FEATURE SCALING"""

#each feature will contribute equally to decision making i.e. finalizing the hypothesis.
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
X_trains = sc_x.fit_transform(X_train)
X_tests = sc_x.transform(X_test)

"""**KNN CLASSIFIER**"""

from sklearn.neighbors import KNeighborsClassifier
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_trains,y_train)

pred = knn_model.predict(X_tests)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,pred)

from sklearn import metrics
confusion_matrix = metrics.confusion_matrix(y_test, pred)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ['female', 'male'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
cl_rep = classification_report(y_test,pred)
print(cl_rep)

"""**DECISION TREE CLASSIFIER**"""

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(max_depth=5)
clf.fit(X_trains, y_train)

y_pred = clf.predict(X_tests)

accuracy_score(y_test,y_pred)

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(70,20))
plot_tree(clf,fontsize=15, filled=True)
plt.title("Decision tree trained on the selected features")
plt.show()

from sklearn import metrics
confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels =['female','male'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
cl_rep = classification_report(y_test,y_pred,labels=['female','male'])
print(cl_rep)

"""**LOGISTIC REGRESSION**"""

from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()

lr.fit(X_trains,y_train)

predi=lr.predict(X_tests)

accuracy_score(y_test,predi)

confusion_matrix = metrics.confusion_matrix(y_test, predi)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels =['female','male'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
cl_rep = classification_report(y_test,predi,labels=['female','male'])
print(cl_rep)

"""**SVM CLASSIFIER**"""

from sklearn import svm

sv = svm.SVC(kernel='linear')

sv.fit(X_trains,y_train)

predic = sv.predict(X_tests)

accuracy_score(y_test,predic)

confusion_matrix = metrics.confusion_matrix(y_test, predic)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels =['female','male'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
cl_rep = classification_report(y_test,predic,labels=['female','male'])
print(cl_rep)

"""**RANDOM FOREST CLASSIFIER**"""

from sklearn.ensemble import RandomForestClassifier
rf =RandomForestClassifier(n_estimators=20)

rf.fit(X_trains,y_train)

ypred=rf.predict(X_tests)

accuracy_score(y_test,ypred)

confusion_matrix = metrics.confusion_matrix(y_test, ypred)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels =['female','male'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
cl_rep = classification_report(y_test,ypred,labels=['female','male'])
print(cl_rep)

"""

From the above evaluated models, we observe that the model which uses the random forest classifies give the most accurate prediction"""