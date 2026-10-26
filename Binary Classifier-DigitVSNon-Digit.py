from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

data = load_digits()
X = data.data
y = np.ones(len(X))

# Create simple non-digit examples
non_digits = np.zeros((len(X), 64))
non_digits[:, 0:8] = 16

X = np.vstack((X, non_digits))
y = np.concatenate((y, np.zeros(len(non_digits))))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Predictions:", pred[:10])
print("Accuracy:", accuracy_score(y_test, pred))