from sklearn.linear_model import LogisticRegression
X=[[20000],[50000],[100000]]
y=[0,0,1]
model=LogisticRegression()
model.fit(X,y)
print(model.predict([[75000]]))
