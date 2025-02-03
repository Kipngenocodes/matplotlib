import matplotlib.pyplot as plt 

import matplotlib
matplotlib.use('QtAgg')

fig = plt.figure(figsize=(4, 2), facecolor='lightskyblue',
                 layout='constrained')
fig.suptitle('Sample Figure')
ax = fig.add_subplot()
ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')

plt.show()