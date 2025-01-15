import matplotlib.pyplot as plt
# Creating a 2x2 grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=2)

# Accessing individual axes (subplots)
axes[0, 0].plot([1, 2, 3], [4, 5, 6])  # Plot in the first subplot (top-left)
axes[0, 1].scatter([1, 2, 3], [4, 5, 6])  # Second subplot (top-right)
axes[1, 0].bar([1, 2, 3], [4, 5, 6])  # Third subplot (bottom-left)
axes[1, 1].hist([1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5])  # Fourth subplot (bottom-right)
plt.show()