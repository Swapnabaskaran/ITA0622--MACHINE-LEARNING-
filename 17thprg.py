from sklearn.linear_model import LinearRegression
X=[[2],[4],[6]]
y=[5000,10000,15000]
model=LinearRegression()
model.fit(X,y)
print(model.predict([[5]]))
