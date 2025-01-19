import  matplotlib.pyplot as  plt
import  numpy as np

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
            

