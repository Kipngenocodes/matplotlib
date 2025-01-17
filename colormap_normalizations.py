import matplotlib as mpl
import numpy as np
from matplotlib.colors import Normalize

'''
 normalization refers to the rescaling of real values to a common range, such as between 0 and 1. 
 It is commonly used as per−processing technique in data processing and analysis.
 Colormap Normalization in Matplotlib:
 Matplotlib provides several methods to normalize data,
 including Min-Max Scaling, Standardization, and Logarithmic
Centered, and Logarithmic scaling, Symmetric logarithmic, Power-law, Discrete Bounds, 
Custom Normalization, and Two-Slope.
The range is typically defined by the minimum (vmin) and maximum (vmax) values 
of the matplotlib.colors.Normalize() instance arguments.
Mapping occurs in two steps, first normalizing the input data to the [0, 1] range and 
then mapping ont the indices in the colormap.
'''
# create a normal object with a specific range
norm = Normalize(vmin=-1, vmax=1)

# normalizing a value 
Normal_value =  norm(0)

# Displaying a normalized value
print(Normal_value)