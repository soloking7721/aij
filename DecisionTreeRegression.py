from sklearn.datasets import make_regression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

X, y = make_regression(
    n_samples=100, n_features=1, noise=10, random_state=1
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

model = DecisionTreeRegressor(random_state=1)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Predictions:", pred[:5])
print("MSE:", mean_squared_error(y_test, pred))