import matplotlib.pyplot as plt

'''
Understanding axes is essential for controlling
and customizing the appearance and behavior of plots in Matplotlib. 
'''

plt.plot([2, 3, 4, 5, 6, 7], [10, 20, 30, 40, 50, 60])

# customizing the limit of axes 
plt.xlim(0,10)
plt.ylim(0, 70)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customizing Axes')
plt.show()

# types of plots 
'''
Line plot: A line plot is a type of graph that displays
    data points connected by straight line segments.
    The plt.plot() function of the matplotlib library is used to create the line plot.

Scatter plot:   A scatter plot is a type of graph that represents individual 
                data points by displaying them as markers on a two-dimensional plane.
                The plt.scatter() function is used to plot the scatter plot.

Line plot:  A line plot is a type of graph that displays data points connected by straight line segments.
            The plt.plot() function of the matplotlib library is used to create the line plot.

Bar plot:   A bar plot or bar chart is a visual representation of categorical data using rectangular bars.
            The plt.bar() function is used to plot the bar plot.

Pie plot:   A pie plot is also known as a pie chart. 
            It is a circular statistical graphic used to illustrate numerical proportions.
            It divides a circle into sectors or slices to represent the relative sizes or percentages of categories within a dataset.
            The plt.pie() function is used to plot the pie chart.
'''