# ITERATE computes and prints the $n$ initial iterates of some function $Q$.\\
# We need to select an initial condition $x$, and number $n$ of iterates to be evaluated.\\
# Use the numpy library to change the given function. A few examples are provided, including an example using a paremeter $m$.\\
# When retyping these, remove the # from whichever function you want to use\\

import numpy as np


def Q(m, x):
    # return np.arccos(x)
    # return m*x*(1-x)
    # return 3*x - 3*x**2
    return (3 + np.sqrt(9 + 12*x))/(-6)


def Iterate(x, n, m, Q):  # Don't forget a value for $m$, even if your function doesn't have a parameter
    pts = [x]
    for i in range(0, n):
        pts.append(Q(m, pts[i]))
    print(pts)


Iterate(-0.2, 100, 1, Q)
