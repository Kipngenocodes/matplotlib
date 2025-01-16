import matplotlib.pyplot as plt 

''' a legend in a graph provides a visual representation of
 the data depicted along the Y-axis, often referred to as the graph series.
 It is a box containing a symbol and a label for each series in the graph
 Very Helpful when having multiple series in a graph '''
 
#  Syntax : plt.legend(*args, **kwargs)
x= [1,2,3,4,5]
y= [2,4,6,8,10]

#plotting the points 
line,  = plt.plot(x,y, label = 'Legend describing a single line')
# Adding a legend
plt.legend()
# Displaying the plot
plt.show()

 