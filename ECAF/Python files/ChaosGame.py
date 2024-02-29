# \% CHAOS GAME selects the midpoint of the line between a given point $(x,y)$ and one\\
# \% of the three given points $B,C,D$.\\
# \% Which of A, B, or C is chosen is random.  The process continues, and\\
# \% eventually yields a (possibly deformed) Sierpinski gasket.  The first 50\\
# \% iterates in the process are ignored.  We need to select the three points\\
# \% A, B, and C, and the initial point (x, y), and the total number n of iterates\\
# \% to be evaluated.\\

import matplotlib.pyplot as plt
import random

# We need an auxilliary function to check if the points are colinear
# B = (b1,b2), C = (c1,c2), D = (d1,d2)
# This computes double the area of a triangle, given these 3 points
# If returns true if the area is zero, meaning the points are colinear.


def colinearCheck(b1, b2, c1, c2, d1, d2):
    a = b1 * (c2 - d2) + c1 * (d2 - b2) + d1 * (b2 - c2)
    return a == 0


# Checks that the point are not colinear, and iterates the function
# The first 50 are ignored, and this returns a list of points to plot


def chaosGame(x, y, b1, b2, c1, c2, d1, d2, n):
    xpts, ypts = [x], [y]
    if colinearCheck(b1, b2, c1, c2, d1, d2):
        print("Points are colinear, change one of them.")
        return
    else:
        for i in range(n):
            r = random.randint(1, 3)
            if r == 1:
                x = (x + b1) / 2
                y = (y + b2) / 2
            elif r == 2:
                x = (x + c1) / 2
                y = (y + c2) / 2
            else:
                x = (x + d1) / 2
                y = (y + d2) / 2
            if i > 50:
                xpts.append(x)
                ypts.append(y)
    return (xpts, ypts)


# Initial conditions for all points and the number of iterations
x0 = 50
y0 = 50
b1 = 0
b2 = 0
c1 = 100
c2 = 0
d1 = 50
d2 = 100
iter = 1000

x, y = chaosGame(x0, y0, b1, b2, c1, c2, d1, d2, iter)
plt.figure(figsize=(5, 5))
plt.scatter(x, y, alpha=1, color="black", s=10)
plt.axis("equal")
plt.axis("off")
plt.show()
