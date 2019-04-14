import pandas as pd
data_set = pd.read_csv("LR.csv")
X=data_set.iloc[:,[0]].values    #IV
Y=data_set.iloc[:,[1]].values   #DV

#fitting Classifier to te Training set
from sklearn.linear_model import LinearRegression
linearRegressor = LinearRegression()
linearRegressor.fit(X,Y)
#predicting the test set result
linearRegressor.score(X,Y)

#Results
import matplotlib.pyplot as plot
plot.scatter(X, Y, color='orange', label='Data')
plot.xlabel('No of hours spent driving', color='white')
plot.ylabel('Risk on scale of 100', color='white')
plot.title('Initial Data', color='white')
plot.xticks(color='white')
plot.yticks(color='white')
plot.legend()
plot.show()
plot.scatter(X, Y, color = 'red')
plot.plot(X, linearRegressor.predict(X), color = 'blue')
plot.title('Title')
plot.xlabel('Number of hours spent driving')
plot.ylabel('Risk score on a scale of 0-100')
plot.show()
