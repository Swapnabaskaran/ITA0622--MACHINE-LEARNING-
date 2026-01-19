from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
X,y=load_iris(return_X_y=True)
model=GaussianNB()
model.fit(X,y)
pred=model.predict(X)
print("Accuracy:",accuracy_score(y,pred))
