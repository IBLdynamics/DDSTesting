
# HENON draws the Henon attractor of $\{\mbox{H}_{\mbox{a}_{.3}}\}$.  It plots from the 51st iterate
# of the initial point (x, y) to the 5000th iterate.  We need to select the
# parameter a and the initial point (x, y).
# The parameter 0.3 is indicated in the comments and could be modified if you wish.

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)


def Henon(a, x, y):
    return 1 - a*x**2 + y


def plot_Henon(a, x, y):  # Parameter $a$ and initial condition $(x,y)$
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title("Henon Attractor")
    ax.plot(x, y, 'ro')  # puts a red circle at the initial condition
    for i in range(1000):
        xt = 1 - a*x**2 + y
        yt = 0.3*x
        x = xt
        y = yt
        if i >= 51:
            ax.plot(x, y, '.k', alpha=0.25)
    plt.show()


plot_Henon(1.4, 0.1, 0.1)
