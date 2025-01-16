import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7, 3.50]
plt.rcParams["figure.autolayout"] = True

# Sample data
x = np.linspace(-2, 2, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Create the figure with subplots
f, axes = plt.subplots(3)

# plot the data on each subplot and add lagend
axes[0].plot(x, y1, c='r', label="sine")
axes[0].legend(loc='upper left')
axes[1].plot(x, y2, c='g', label="cosine")
axes[1].legend(loc='upper left')
axes[2].plot(x, y3, c='b', label="tan")
axes[2].legend(loc='upper left')

# Display the figure
plt.show()