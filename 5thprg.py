from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
X,y=load_iris(return_X_y=True)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X,y)
print(knn.predict([X[0]]))
