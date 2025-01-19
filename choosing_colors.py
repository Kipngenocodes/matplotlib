import  matplotlib.pyplot as  plt
import  numpy as np
import matplotlib as mpl

'''
Choosing an appropriate colormap involves finding a suitable representation in 3D colorspace for your dataset.
The factors for selecting an appropriate colormap for any given data set include −
    Nature of Data − Whether representing form or metric data
    Knowledge of the Dataset − Understanding the dataset's characteristics.
    Intuitive Color Scheme − Considering if there's an intuitive color scheme for the parameter being plotted.
    Field Standards − Considering if there is a standard in the field the audience may be expecting.'''
    
# Categories of colormaps
'''
Categories of Colormaps
Sequential − Incremental changes in lightness and saturation, 
            often using a single hue. Suitable for representing ordered information.
Diverging − Changes in lightness and saturation of two colors, 
            meeting at an unsaturated color. Ideal for data with a critical middle value,
            like topography or data deviating around zero.
Cyclic − Changes in the lightness of two colors, 
        meeting at the middle and beginning/end at an unsaturated color. 
        Suitable for values that wrap around at endpoints, such as phase angle or time of day.
Qualitative − Miscellaneous colors with no specific order. 
            Used for representing information without ordering or relationships.'''
            
# List of Sequential colormaps to visualize
cmap_list = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
   'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
   'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']

# Plot the color gradients

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

# Create figure and adjust figure height to the number of colormaps
nrows = len(cmap_list)
figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
fig, axs = plt.subplots(nrows=nrows + 1, figsize=(7, figh))
fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,
   left=0.2, right=0.99)
axs[0].set_title('Sequential colormaps', fontsize=14)

for ax, name in zip(axs, cmap_list):
   ax.imshow(gradient, aspect='auto', cmap=mpl.colormaps[name])
   ax.text(-0.1, 0.5, name, va='center', ha='right', fontsize=10,
      transform=ax.transAxes)

