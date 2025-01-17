import  matplotlib.pyplot as plt
import  numpy as np
from matplotlib.colors import LinearSegmentedColormap
import matplotlib as mpl

# Creating a LinearSegmentedColormap from a list
colors = ["rosybrown", "gold", "lawngreen", "linen"]
cmap_from_list = [LinearSegmentedColormap.from_list("SmoothCmap", colors)]

# Plotting examples
np.random.seed(19680801)
data = np.random.randn(30, 30)
n = len(cmap_from_list)

fig, axs = plt.subplots(1, n, figsize=(7, 3), layout='constrained', squeeze=False)
for [ax, cmap] in zip(axs.flat, cmap_from_list):
   psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
   fig.colorbar(psm, ax=ax)

plt.show()