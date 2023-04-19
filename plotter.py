import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

num_points = 100
dimensions = 1

weights = np.random.uniform(-1, 1, size=dimensions + 1)
features = np.random.uniform(-1, 1, size=(num_points, dimensions))
features = np.c_[features, np.ones((num_points, 1))]  # Add a bias term
labels = np.dot(features, weights) + np.random.uniform(-0.5, 0.5, size=num_points)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=(dimensions + 1,)))
model.compile(optimizer='adam', loss='mse')
model.fit(features, labels, epochs=10, verbose=0)


x_min, x_max = features[:, 0].min() - 1, features[:, 0].max() + 1
y_min, y_max = labels.min() - 1, labels.max() + 1
xs = np.linspace(x_min, x_max, 100)
ys = model.predict(np.c_[xs, np.ones(xs.shape)])
plt.plot(xs, ys, 'r', linewidth=2)
plt.scatter(features[:, 0], labels)
plt.show()
