import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt

# Create data 
X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
# Creating subplots
fig, ax = plt.subplots(1, 2, figsize=(7,4), layout='constrained')

# Logarithmic Normalizations
pc = ax[0].imshow(Z**2 * 100, cmap='plasma',
   norm=colors.LogNorm(vmin=0.01, vmax=100))
fig.colorbar(pc, ax=ax[0], extend='both')
ax[0].set_title('Logarithmic Normalization')

# Linear Normalization
pc = ax[1].imshow(Z**2 * 100, cmap='plasma',
   norm=colors.Normalize(vmin=0.01, vmax=100))
fig.colorbar(pc, ax=ax[1], extend='both')
ax[1].set_title('Linear Normalization')
plt.show()