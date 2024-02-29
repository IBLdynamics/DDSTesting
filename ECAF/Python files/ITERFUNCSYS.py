# ITERFUNCSYS plots the iterates in the Iterated Function System given by three\\
# functions that are defined in the program. \\
# For each $k$, one of the three given functions is chosen randomly and the $k$th iterate \\
# of the initial point $(x, y)$ is plotted.  The resulting figure is the Sierpinski gasket. \\
# We need to select the initial point $(x_0, y_0)$, as well as the total number of $n$ iterates \\
# to be evaluated.\\

import matplotlib.pyplot as plt
import numpy as np
import random

# We can define a function $T$ for our iterated system. The code below differentiates each $T$
# Input the values for the point you wish to transform
# and the 6 parameters from section 6.4 of the text.


def T(x, y, a, b, c, d, e, f):
    return [a * x + b * y + e, c * x + d * y + f]


def IFS(x, y, n):
    xpts, ypts = [], []
    for i in range(n):
        r = random.randint(1, 3)
        if r == 1:
            x = T(x, y, 0.5, 0, 0, 0.5, 0, 0)[0]
            y = T(x, y, 0.5, 0, 0, 0.5, 0, 0)[1]
        elif r == 2:
            x = T(x, y, 0.5, 0, 0, 0.5, 0.5, 0)[0]
            y = T(x, y, 0.5, 0, 0, 0.5, 0.5, 0)[1]
        else:
            x = T(x, y, 0.5, 0, 0, 0.5, 0.25, np.sqrt(3) / 4)[0]
            y = T(x, y, 0.5, 0, 0, 0.5, 0.25, np.sqrt(3) / 4)[1]
        if i > 100:
            xpts.append(x)
            ypts.append(y)
    return (xpts, ypts)


# Initial conditions and number of loops to run
x0 = 0
y0 = 0
iter = 10000

x, y = IFS(x0, y0, iter)
plt.figure(figsize=(5, 5))
plt.scatter(x, y, color="black", s=10)
plt.axis("equal")
plt.axis("off")
plt.show()
