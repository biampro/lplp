from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt 
import pandas as pd
df=pd.read_csv('ass3.csv')
x=df.drop(['labels'],axis=1)
y=df['labels']
print(df.info())
orange=df[df["labels"]=="orange"]
blue=df[df["labels"]=="blue"]
plt.scatter(orange.iloc[:,0].values,orange.iloc[:,1].values,color='orange')
plt.scatter(blue.iloc[:,0].values,blue.iloc[:,1].values,color='blue')
plt.scatter(6,6,color='black')
plt.show()
model= KNeighborsClassifier(n_neighbors=3)
model.fit(x,y)
print("class of (6,6) is")
print(model.predict([[6,6]]))
