import matplotlib.pyplot as plt
import numpy as np

# Create a Bar Plot
categories = ['A', 'B', 'C']
values = [3, 7, 5]
plt.bar(categories, values)
plt.title("Bar Plot")
plt.show()

# Create a Horizontal Bar Plot
plt.barh(categories, values)
plt.title("Horizontal Bar Plot")
plt.show()

# Create a Box Plot
data = np.random.rand(50)
plt.boxplot(data)
plt.title("Box Plot")
plt.show()

# Create a Histogram
data = np.random.randn(1000)
plt.hist(data, bins=20)
plt.title("Histogram")
plt.show()

# Create a 2D Histogram
x = np.random.randn(1000)
y = np.random.randn(1000)
hist2d = plt.hist2d(x, y, bins=30)
plt.title("2D Histogram")
plt.colorbar(hist2d[3])  # Add a colorbar for the 2D histogram
plt.show()

# Create a Pie Chart
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# Create a Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Line Plot")
plt.show()

# Create a Polar Plot
theta = np.linspace(0, 2 * np.pi, 100)
r = 1 + np.sin(4 * theta)
plt.subplot(projection='polar')
plt.plot(theta, r)
plt.title("Polar Plot")
plt.show()

# Create a Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# Create a Stacked Area Plot
x = np.arange(0, 10, 1)
y1 = x
y2 = x**2
y3 = x**3
plt.stackplot(x, y1, y2, y3, labels=["Linear", "Quadratic", "Cubic"])
plt.legend(loc='upper left')
plt.title("Stacked Area Plot")
plt.show()

# Create a Stem Plot
x = np.linspace(0, 10, 10)
y = np.sin(x)
plt.stem(x, y)
plt.title("Stem Plot")
plt.show()

# Create a Step Plot
x = np.arange(5)
y = [3, 7, 5, 8, 4]
plt.step(x, y)
plt.title("Step Plot")
plt.show()

# Create a Quiver Plot
x, y = np.meshgrid(np.arange(-2, 2, 0.5), np.arange(-2, 2, 0.5))
u = -y
v = x
plt.quiver(x, y, u, v)
plt.title("Quiver Plot")
plt.show()
