import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 1, 0, 1]
]

y = ["Cat", "Dog", "Cat", "Dog"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

model = RandomForestClassifier()
model.fit(X_train, y_train)

prediction = model.predict(X_test)
print("Predicted Output:", prediction)