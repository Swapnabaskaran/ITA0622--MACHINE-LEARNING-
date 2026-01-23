from sklearn.linear_model import LinearRegression
X=[[2019],[2020],[2021]]
y=[200,250,300]
model=LinearRegression()
model.fit(X,y)
print(model.predict([[2022]]))
