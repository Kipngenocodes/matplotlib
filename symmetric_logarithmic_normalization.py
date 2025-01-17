import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors, cm

X, Y = np.mgrid[-3:3:complex(0, 128), -2:2:complex(0, 128)]
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(7, 4), layout='constrained')

# Symmetric Logarithmic Normalization
pcm = ax[0].pcolormesh(X, Y, Z, 
   norm=colors.SymLogNorm(linthresh=0.03, linscale=0.03,vmin=-1.0, vmax=1.0, base=10),
   cmap='plasma', shading='auto')
fig.colorbar(pcm, ax=ax[0])
ax[0].set_title('SymLogNorm()')

# Default Linear Normalization
pcm = ax[1].pcolormesh(X, Y, Z, cmap='plasma', vmin=-np.max(Z), shading='auto')
fig.colorbar(pcm, ax=ax[1])
ax[1].set_title('Normalize')

plt.show()