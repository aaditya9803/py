import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
num_points = 100
dimensions = 2

# Define the pitfall function
def pitfall(x):
    return (x[:, 0] - 0.5)**2 + (x[:, 1] - 0.5)**2 - 0.25

# Sample random points around the pitfall
features = np.random.uniform(0, 1, size=(num_points, dimensions))
labels = pitfall(features)

# Sort the points by the pitfall function value
sorted_indices = np.argsort(labels)
features, labels = features[sorted_indices], labels[sorted_indices]

# Fit a linear model using Gradient Descent
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=(dimensions,)))
model.compile(optimizer='adam', loss='mse')
history = model.fit(features, labels, epochs=100, verbose=0)

# Plot the optimization path
plt.plot(history.history['loss'])
plt.title('Gradient Descent')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.show()

# Fit a linear model using Pitfall optimization
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=(dimensions,)))
optimizer = tf.keras.optimizers.SGD(learning_rate=0.1, momentum=0.9)
model.compile(optimizer=optimizer, loss='mse')
history = model.fit(features, labels, epochs=100, verbose=0)

# Plot the optimization path
plt.plot(history.history['loss'])
plt.title('Pitfall optimization')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.show()