import matplotlib.pyplot as plt 

# checking for the available styles in the matplotlib library
print(plt.style.available)

# Applying specific style to the plot

# Create a simple plot
plt.style.use('seaborn-v0_8-pastel')
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot with seaborn-v0_8-pastel syle')
plt.show()
