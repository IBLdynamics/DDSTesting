
# TINKERBELL draws the Tinkerbell attractor. It plots from the 51st iterate
# of the initial point (x, y) to the 5000th iterate.  We need to select the
# parameters $a,b,c,d$ and the initial point $(x_0, y_0)$.
#

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

# Parameters $a,b,c$ and $d$ and initial condition $(x,y)$


def plot_Tinkerbell(a, b, c, d, x, y):
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2.5, 1.5)
    ax.set_title("Tinkerbell Attractor")
    for i in range(5000):
        xt = x**2 - y**2 + a*x + b*y
        yt = 2*x*y + c*x + d*y
        x = xt
        y = yt
        if i >= 51:
            ax.plot(x, y, '.k', alpha=0.25)
    plt.show()


# Initial Conditions
a = 0.9
b = -0.6013
c = 2
d = 0.5
x0 = 0.01
y0 = 0.01

plot_Tinkerbell(a, b, c, d, x0, y0)
