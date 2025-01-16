import matplotlib.pyplot as plt
import numpy as np


'''
Format in which an image can be saved 
png
svg
jpeg
pdf'''

# Example of implementation of the steps of creating a plot and saving it in different  formats
# 1. Data Preparations
x = np.linspace(0, 10, 100)  # Generate 100 evenly spaced
y = np.sin(x)  # Generate sine wave data
y2 = np.cos(x)  # Generate cosine wave data
# 2. Plotting the functions
plt.plot(x, y, label='Sine wave')  # Plot the sine wave
plt.plot(x, y2, label='Cosine wave')  # Plot the cosine wave
# 3. Customizations of label
plt.xlabel('X-axis')  # Set the label of the x-axis
plt.ylabel('Y-axis')  # Set the label of the y-axis
plt.title('Sine and Cosine wave')  # Set the title of the plot
# 4. Displaying the plot
plt.legend()  # Display the legend of the plot
# Saving an output as png
plt.savefig(r'C:\Users\p1\OneDrive\Desktop\matplotlib\sample.png')
# Saving an output as svg
plt.savefig(r'C:\Users\p1\OneDrive\Desktop\matplotlib\sample.svg')
# Saving an output as pdf
plt.savefig(r'C:\Users\p1\OneDrive\Desktop\matplotlib\sample.pdf')
# Saving an output as jpeg
plt.savefig(r'C:\Users\p1\OneDrive\Desktop\matplotlib\sample.jpeg')

plt.show()  # Display the plot


