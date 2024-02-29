# BIFURCATION plots the bifurcation diagram of the quadratic family $Q_m$
# for m in [p,q] by increments of 0.001. Select the min value and max
# value of the window, and the value for the parameter m

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)


def Q(x, m):  # The bifurcation here is for a specific function, so leave this alone
    return m * x * (1 - x)


def Bifurcation(p, q):  # For the interval [p,q] with function $Q_m$.
    ax.set_xlim(p, q)
    ax.set_title("Bifurcation diagram")
    n = int((q - p) / 0.001)  # Number of points for the horizontal axis
    r = np.linspace(p, q, n)
    iterations = 1000
    last = 100  # Takes 1000 iterations, and only shows the last 100
    x = 0.01 * np.ones(n)  # defines a lit of initial conditions
    for i in range(iterations):
        x = Q(x, r)
        if i >= (iterations - last):
            ax.plot(r, x, ",k", alpha=1, markersize=10)
    plt.show()


Bifurcation(2.95, 3.6)
