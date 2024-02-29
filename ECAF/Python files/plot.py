# PLOT plots the indicated function and the line y = x\\

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh')
# Change the values below the adjust the axes, depending on your function.
xmin = -0.1
xmax = 1.1
ymin = -0.1
ymax = 1.1

ticks = 0.1  # Change this to indicate how often you want the ticks to show up on each axis


def Q(x, m):  # As in the previous program, define your function. You may ignore the parameter if it is not used
    # return np.cos(x)
    return m*x*(1-x)
    # return 3*x - 3*x**2
    # return (3 + np.sqrt(9 + 12*x))/(-6)


# defines 60 evenly spaced values along the x-axis
x = np.linspace(xmin, xmax, 60)
y = Q(x, 3)  # Computes the correponding y-values

# Defines the area for the plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0, color='black')  # plots the function
ax.plot(x, x, linewidth=2.0, color='red')  # plots the diagonal

# sets the limits for the axes and tickmarks
ax.set(xlim=(xmin, xmax), xticks=np.arange(xmin + ticks, xmax, ticks),
       ylim=(ymin, ymax), yticks=np.arange(ymin + ticks, ymax, ticks))

# Shows the graph in a new window
plt.show()
