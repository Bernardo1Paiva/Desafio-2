# -*- coding: utf-8 -*-
"""untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/Bernardo1Paiva/c6c762f106cff5165358a0c7026faece/untitled0.ipynb
"""



import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# URLs dos dados
train_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data'
test_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-testing.data'

# Carregamento dos dados
train_data = pd.read_csv(train_url, header=None)
test_data = pd.read_csv(test_url, header=None)

# Preparando os dados
X_train = train_data.iloc[:, :-1].values
y_train = train_data.iloc[:, -1].values
X_test = test_data.iloc[:, :-1].values
y_test = test_data.iloc[:, -1].values

# Convertendo as classes para categórico
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Criar o modelo
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(y_train.shape[1], activation='softmax'))

# Compilar o modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Treinar o modelo
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Avaliar o modelo
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {test_accuracy}')