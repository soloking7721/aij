from sklearn.datasets import load_iris
from collections import Counter

data = load_iris()

x = data.data
y = data.target

count = Counter(y)

print("Class Distribution:", count)

for i, n in count.items():
    print(data.target_names[i], ":", n)
