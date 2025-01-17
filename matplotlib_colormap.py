import matplotlib.pyplot as plt 
import matplotlib
import numpy as np 

# Checking a colormap
# print(list(matplotlib.colormaps))

# accessing the colormaps 
viridis = matplotlib.colormaps['viridis'].resampled(8)
print(viridis)