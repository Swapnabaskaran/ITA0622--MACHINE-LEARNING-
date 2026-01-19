from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
X,y=load_iris(return_X_y=True)
clf=MLPClassifier(hidden_layer_sizes=(5,),max_iter=1000)
clf.fit(X,y)
print("Accuracy:",clf.score(X,y))
