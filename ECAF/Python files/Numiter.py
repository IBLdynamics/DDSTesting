# NUMITER computes the iterates of a function $Q$ until an iterate is within $d$ \\
# of $p$.  We need to select the initial point $x$, fixed point or  \\
# periodic point $p$, the maximum allowed distance $d$ between the desired \\
# iterate and $p$, and maximum number $n$ of iterates to be evaluated. \\ \\

import numpy as np


def Q(x, m):  # As in the previous program, define your function. You may ignore the parameter if it is not used
    # return np.cos(x)
    return m*x*(1-x)
    # return 3*x - 3*x**2
    # return (3 + np.sqrt(9 + 12*x))/(-6)


# If your function didn't have a parameter, you can skip a value for $m$
def Numiter(x, p, d, n, Q, m=1):
    iter = 0
    while np.abs(x-p) > d and iter <= n:
        x = Q(x, m)
        iter += 1
    if iter >= n:
        print("After " + str(n) +
              " iterations the distance is still " + str(np.abs(x-p)))
    else:
        print("After " + str(iter) +
              " iterations the distance is less than " + str(d))


Numiter(0.5, 0.666, 0.001, 100000, Q, 4)
