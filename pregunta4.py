import tensorflow as tf
import numpy as np

x = np.array([[1],[2],[3],[4],[5]])
y = np.array([2,4,6,8,10]) 

modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])
modelo.compile(optimizer='sgd', loss='mse')
modelo.fit(x, y, epochs=200, verbose=0)

print(modelo.predict(np.array([[10],[15]])))
