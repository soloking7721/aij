from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, KFold

data = load_iris()
X, y = data.data, data.target

model = DecisionTreeClassifier(random_state=1)
kf = KFold(n_splits=5, shuffle=True, random_state=1)

scores = cross_val_score(model, X, y, cv=kf)

print("Validation scores:", scores)
print("Mean accuracy:", scores.mean())