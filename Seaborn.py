import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data
x_values = np.linspace(0, 10, 100)  # Generate 100 points from 0 to 10
y_values = np.sin(x_values)         # Compute the sine of each point

# Create a line plot using Seaborn
sns.lineplot(x=x_values, y=y_values)

# Show the plot
plt.show()
