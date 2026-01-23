from sklearn.linear_model import LinearRegression
X=[[1],[2],[3]]
y=[10000,15000,20000]
model=LinearRegression()
model.fit(X,y)
print(model.predict([[4]]))
