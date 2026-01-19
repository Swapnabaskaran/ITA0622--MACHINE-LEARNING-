import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
X=np.array([[1],[2],[3],[4]])
y=np.array([1,4,9,16])
poly=PolynomialFeatures(2)
Xp=poly.fit_transform(X)
model=LinearRegression()
model.fit(Xp,y)
print(model.predict(poly.transform([[5]])))
