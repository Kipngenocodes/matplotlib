import matplotlib.pyplot as plt
import numpy as np

# Create a grid of subplots
fig, axes = plt.subplots(7, 2, figsize=(15, 20))  # 7 rows, 2 columns
axes = axes.flatten()  # Flatten to make indexing easier

#   Create a Bar Plot
categories = ['A', 'B', 'C']
values = [3, 7, 5]
axes[0].bar(categories, values)
axes[0].set_title("Bar Plot")

#  Create a Horizontal Bar Plot
axes[1].barh(categories, values)
axes[1].set_title("Horizontal Bar Plot")

#  Create a Box Plot
data = np.random.rand(50)
axes[2].boxplot(data)
axes[2].set_title("Box Plot")

# Create a Histogram
data = np.random.randn(1000)
axes[3].hist(data, bins=20)
axes[3].set_title("Histogram")

#  Create a 2D Histogram
x = np.random.randn(1000)
y = np.random.randn(1000)
hist2d = axes[4].hist2d(x, y, bins=30)
axes[4].set_title("2D Histogram")
fig.colorbar(hist2d[3], ax=axes[4])  # Add a colorbar for the 2D histogram

#  Create a Pie Chart
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
axes[5].pie(sizes, labels=labels, autopct='%1.1f%%')
axes[5].set_title("Pie Chart")

#  Create a Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
axes[6].plot(x, y)
axes[6].set_title("Line Plot")

#  Create a Polar Plot
theta = np.linspace(0, 2 * np.pi, 100)
r = 1 + np.sin(4 * theta)
axes[7].polar(theta, r)
axes[7].set_title("Polar Plot")

#  Create a Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
axes[8].scatter(x, y)
axes[8].set_title("Scatter Plot")

#  Create a Stacked Area Plot
x = np.arange(0, 10, 1)
y1 = x
y2 = x**2
y3 = x**3
axes[9].stackplot(x, y1, y2, y3, labels=["Linear", "Quadratic", "Cubic"])
axes[9].legend(loc='upper left')
axes[9].set_title("Stacked Area Plot")

#  Create a Stem Plot
x = np.linspace(0, 10, 10)
y = np.sin(x)
axes[10].stem(x, y)
axes[10].set_title("Stem Plot")

#  Create a Step Plot
x = np.arange(5)
y = [3, 7, 5, 8, 4]
axes[11].step(x, y)
axes[11].set_title("Step Plot")

#  Create a Quiver Plot
x, y = np.meshgrid(np.arange(-2, 2, 0.5), np.arange(-2, 2, 0.5))
u = -y
v = x
axes[12].quiver(x, y, u, v)
axes[12].set_title("Quiver Plot")

# Hide the unused subplot
axes[13].axis('off')

# Adjust layout
plt.tight_layout()
plt.show()
