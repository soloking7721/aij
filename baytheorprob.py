prior = 0.01
sensitivity = 0.90
false_positive = 0.05

p = (sensitivity * prior) / (
    sensitivity * prior +
    false_positive * (1 - prior)
)

print("Disease Probability:", round(p * 100, 2), "%")
