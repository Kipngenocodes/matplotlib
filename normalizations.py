import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors, cm

'''
This normalization is useful to remap colors onto a 
power-law relationship using the colors.PowerNorm() class.'''

X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
Z = (1 + np.sin(Y * 10.)) * X**2

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(7, 4), layout='constrained')

# Power-law Normalization
pcm = ax[0].pcolormesh(X, Y, Z, norm=colors.PowerNorm(gamma=0.5),
   cmap='PuBu_r', shading='auto')
fig.colorbar(pcm, ax=ax[0])
ax[0].set_title('PowerNorm()')

# Default Linear Normalization
pcm = ax[1].pcolormesh(X, Y, Z, cmap='PuBu_r', shading='auto')
fig.colorbar(pcm, ax=ax[1])
ax[1].set_title('Normalize')

plt.show()