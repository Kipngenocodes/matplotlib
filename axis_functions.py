import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a figure and axes
fig, ax = plt.subplots()  # Axes function: Create axes within a figure

# Plot the data
ax.plot(x, y, label="Sine Wave")

# Adding title and labels
ax.set_title("Demonstration of Axis Functions")  # Title
ax.set_xlabel("X-axis (Time)")  # Xlabel
ax.set_ylabel("Y-axis (Amplitude)")  # Ylabel

# Set x and y limits
ax.set_xlim(0, 10)  # Xlim
ax.set_ylim(-1.5, 1.5)  # Ylim

# Customize scale
ax.set_xscale('linear')  # Xscale (set linear scaling for X-axis)
ax.set_yscale('linear')  # Yscale (set linear scaling for Y-axis)

# Customize ticks
ax.set_xticks([0, 2, 4, 6, 8, 10])  # Xticks: Setting custom tick locations for X-axis
ax.set_xticklabels(["Zero", "Two", "Four", "Six", "Eight", "Ten"])  # Custom labels for X ticks
ax.set_yticks([-1, 0, 1])  # Yticks: Setting custom tick locations for Y-axis
ax.set_yticklabels(["Low", "Neutral", "High"])  # Custom labels for Y ticks

# Add text annotation
ax.text(5, 0, "Center Point", color="red", fontsize=12)  # Text: Adding custom text to the plot

# Add a legend
ax.legend()

# Display the plot
plt.show()
