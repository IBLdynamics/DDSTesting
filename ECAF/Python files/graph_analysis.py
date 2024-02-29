# PLOT plots the indicated function and the line y = x\\
# For a given initial condition, shows the graphical analysis for the orbit of that point.

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh')
# Change the values below the adjust the axes, depending on your function.
xmin = -0.1
xmax = 1.1
ymin = -0.1
ymax = 1.1

ticks = 0.1  # Change this to indicate how often you want the ticks to show up on each axis

ic = 0.1  # Choose the initial condition for your input
orbit = 20  # Choose how many steps you want in your orbit


def Q(x, m=1):  # As in the previous program, define your function.
    # You may ignore the parameter if it is not used. Some examples are included.
    # return np.cos(x)
    return m*x*(1-x)
    # return 3*x - 3*x**2
    # return (3 + np.sqrt(9 + 12*x))/(-6)


# Choose your function, initial condition, and how many steps you want.
def pts(Q, ic, orbit, m=1):
    xpts = [ic]
    ypts = [0]
    for i in range(0, orbit*2, 2):
        xpts.append(xpts[i])
        ypts.append(Q(xpts[i], m))
        xpts.append(ypts[i+1])
        ypts.append(ypts[i+1])
    return [xpts, ypts]


# defines 60 evenly spaced values along the x-axis
x = np.linspace(xmin, xmax, 60)
m = 0.5
y = Q(x, m)  # Computes the correponding y-values

# Defines the area for the plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0, color='black')  # plots the function
ax.plot(x, x, linewidth=2.0, color='red')  # plots the diagonal

xpts = pts(Q, ic, orbit, m)[0]
ypts = pts(Q, ic, orbit, m)[1]
ax.plot(xpts, ypts, linewidth=2.0)  # plots orbit

# Sets the limits for the axes and tickmarks
ax.set(xlim=(xmin, xmax), xticks=np.arange(xmin + ticks, xmax, ticks),
       ylim=(ymin, ymax), yticks=np.arange(ymin + ticks, ymax, ticks))

# Shows the graph in a new window
plt.show()
