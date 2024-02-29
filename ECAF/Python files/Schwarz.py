# This should compute the Schwazian derivative for $f(x) = ax^n e^{-bx}$.
# Show it's negative, and give iterations and graphical analysis

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons
import sympy as sym
from sympy.abc import a, b, n, x  # defines variables
from sympy import diff, exp  # exponential function
from sympy.plotting import plot

f = a*x**n*exp(-b*x)
f1 = diff(f, x)
f2 = diff(f1, x)
f3 = diff(f2, x)
S = f3/f1 - 1.5*(f2/f1)**2
S_eval = sym.lambdify(args=[x, a, b, n], expr=S)

# Change these values to alter the max and min for the x-axis. Exclude zero.
xmin = 0.01
xmax = 10
x = np.linspace(xmin, xmax, 60)
# Change the parameters a,b, and n below.
# These are renamed to separate them from the symbolic variables
sa = 3
sb = 4
sn = 7
y = S_eval(x, sa, sb, sn)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
