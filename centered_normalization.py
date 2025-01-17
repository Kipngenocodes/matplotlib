import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors, cm

'''
When data is symmetrical around a center (e.g., positive and negative anomalies around 0), the colors.
CenteredNorm() class can be used. It automatically maps the center to 0.5, 
and the point with the largest deviation from the center to 1.0 or 0.0, depending on its value.
'''

X, Y = np.meshgrid(np.linspace(-3, 3, 150), np.linspace(-3, 3, 150))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

# Select the divergent  colormap
cmap = cm.coolwarm 

# Create a subplots 
fig, ax = plt.subplots(1, 2, figsize=(12, 6), layout ='constrained')

# Create a default linear normalizations 
pc = ax[0].pcolormesh(X, cmap=cmap, shading=' auto')
fig.colorbar(pc, ax=ax[0])
ax[0].set_title('Normalize')

# create a centered normalizations
pc = ax[1].pcolormesh(Z, norm=colors.CenteredNorm(), cmap=cmap)
fig.colorbar(pc, ax=ax[1])
ax[1].set_title('CenteredNorm()')

plt.show()