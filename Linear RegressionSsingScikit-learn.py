from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

model = LinearRegression()
model.fit(X, y)

pred = model.predict([[6], [7]])

print("Predictions:", pred)
print("MSE:", mean_squared_error([12, 14], pred))