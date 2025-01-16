import matplotlib.pyplot as plt
import numpy as np

'''
Matplotlib markers are used to highlight individual data points on a plot. 
The marker parameter in the plot() function is used to specify the marker style.
        Types of the Markers
a.  ‘o’ circle
b.  ‘^’ triangle_up
c.  ‘v’ triangle_down
d.  ‘s’ square
e.  ‘D’ diamond
f.  ‘+’ plus
g.  ‘x’ cross
h.  ‘*’ star
i.  ‘.’ point
j.  ‘1’ tri_down
k.  ‘2’ tri_up
l.  ‘3’ tri_left
m.  ‘4’ tri_right
n.  ‘8’ octagon

'''

# syntax = plt.plot(x, y, marker='marker_style')

# Data
x = [22,1,7,2,21,11,14,5]
y = [24,2,12,5,5,5,9,12]
plt.plot(x,y, marker = 'v')

# Customize the plot (optional)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(' Line Plot with triangular marker')

# Display the plot
plt.show()