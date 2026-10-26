from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X = [
    ['Sunny', 'Hot'], ['Sunny', 'Mild'],
    ['Rainy', 'Cool'], ['Rainy', 'Mild'],
    ['Overcast', 'Hot'], ['Overcast', 'Cool'],
    ['Sunny', 'Cool'], ['Rainy', 'Hot'],
    ['Overcast', 'Mild'], ['Sunny', 'Hot']
]
y = ['No', 'No', 'Yes', 'Yes', 'Yes',
     'Yes', 'Yes', 'No', 'Yes', 'No']

le = LabelEncoder()
X = [le.fit_transform(col) for col in zip(*X)]
X = list(map(list, zip(*X)))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = GaussianNB()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Predictions:", pred)
print("Accuracy:", accuracy_score(y_test, pred))