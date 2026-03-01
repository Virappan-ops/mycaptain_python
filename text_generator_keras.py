import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.utils import to_categorical

text = "hello world"
text = text.lower()

chars = sorted(list(set(text)))
char_to_int = {c: i for i, c in enumerate(chars)}
int_to_char = {i: c for i, c in enumerate(chars)}

X = []
y = []

for i in range(len(text) - 1):
    X.append(char_to_int[text[i]])
    y.append(char_to_int[text[i + 1]])

X = np.array(X)
y = to_categorical(y)

X = np.reshape(X, (X.shape[0], 1, 1))
X = X / float(len(chars))

model = Sequential()
model.add(LSTM(50, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(y.shape[1], activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

model.fit(X, y, epochs=100, batch_size=1, verbose=2)

start = X[0]
pattern = [int(start[0][0] * len(chars))]

print("Generated Text:")
for i in range(20):
    x = np.reshape(pattern[-1], (1, 1, 1)) / float(len(chars))
    prediction = model.predict(x, verbose=0)
    index = np.argmax(prediction)
    result = int_to_char[index]
    print(result, end="")
    pattern.append(index)