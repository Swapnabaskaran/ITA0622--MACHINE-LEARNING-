from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
X,y=load_iris(return_X_y=True)
lr=LogisticRegression(max_iter=200)
lr.fit(X,y)
print("Accuracy:",lr.score(X,y))
