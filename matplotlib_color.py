import matplotlib.pyplot as plt
import numpy as np

# Generate data for the sine wave
x = np.linspace(-10, 10, 500)  # X values
y = np.sin(x)  # Y values (sine wave)

# Apply a seaborn style and configure the plot
plt.style.use('seaborn-v0_8-pastel')
plt.figure(figsize=(10, 6))
plt.title('Plotting a Sine Wave')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)  # Enable gridlines

# Add reference lines at x=0 and y=0
plt.axhline(0, color='black', linestyle='--', linewidth=1)  # Horizontal line
plt.axvline(0, color='black', linestyle='--', linewidth=1)  # Vertical line

# Plot the sine wave with a blue color
plt.plot(x, y, color='blue', label='sin(x)')

# Add a legend for clarity
plt.legend()

# Display the plot
plt.show()

# usinf the The Hex RGB or RGBA String format to set the color
# Example of data
t = np.linspace(0.0, 2.0, 201)
y = np.sin(t)

# Hex string for specifying axis facecolor
fig, ax = plt.subplots(figsize = (10,6))
ax.set_facecolor("#eafff5")

# Plotting the sine wave and Data
plt.plot(t, y)

# Showing the graph
plt.show()
