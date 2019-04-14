import pandas as pd
data_set = pd.read_csv("Customer.csv")
from sklearn.preprocessing import LabelEncoder
import numpy as np
X=data_set.iloc[:,[1,2,3,4]].values #IV
Y=data_set.iloc[:,5].values #DV
x_pred = np.array(['<21', 'Low', 'Female', 'Married'])#we can take it from user
#Label Encoding
le = LabelEncoder()
x_pred = le.fit_transform(x_pred)
for i in range(4):
	X[:,i] = le.fit_transform(X[:,i])
Y = le.fit_transform(Y)
#fitting Classifier to the Training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(X,Y)
#predicting the test set result
y_pred= classifier.predict([x_pred])
#Results
print("-----FOR AGE<21, INCOME = LOW, GENDER = FEMALE AND MARITAL STATUS = MARRIED.....")
print("The Decision is : ")
print(le.inverse_transform(y_pred))
