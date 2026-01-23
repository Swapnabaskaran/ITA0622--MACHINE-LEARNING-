from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
X,y=load_iris(return_X_y=True)
print(LogisticRegression(max_iter=200).fit(X,y).score(X,y))
print(GaussianNB().fit(X,y).score(X,y))
