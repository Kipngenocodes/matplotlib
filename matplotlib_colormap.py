import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.colors import ListedColormap

# List of colormap names to iterate through
colormap_names = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']

# Generate random data for visualization
np.random.seed(42)
data = np.random.rand(10, 10)  # Example 2D data

# Create a figure and axes for subplots
fig, axes = plt.subplots(1, len(colormap_names), figsize=(15, 4), constrained_layout=True)

# Loop through the colormap names and plot the data using each colormap
for ax, cmap_name in zip(axes, colormap_names):
    cmap = matplotlib.colormaps[cmap_name]  # Access the colormap
    psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=0, vmax=1)
    ax.set_title(cmap_name)  # Set the title to the colormap name
    fig.colorbar(psm, ax=ax)

# Show the plots
plt.show()
