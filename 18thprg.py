from sklearn.linear_model import Perceptron
from sklearn.datasets import load_iris
X,y=load_iris(return_X_y=True)
model=Perceptron()
model.fit(X,y)
print(model.score(X,y))
