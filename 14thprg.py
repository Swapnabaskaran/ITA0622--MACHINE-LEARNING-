from sklearn.linear_model import LinearRegression
X=[[500],[1000],[1500]]
y=[50,100,150]
model=LinearRegression()
model.fit(X,y)
print(model.predict([[2000]]))
