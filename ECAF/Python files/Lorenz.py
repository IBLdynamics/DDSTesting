# Plots the Lorentz attractor.

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Since we're making a 3d image, it's important to set up
# the screen correctly
WIDTH, HEIGHT, DPI = 1000, 750, 100

# Lorenz paramters and initial conditions.
sigma, b, r = 10, 2.667, 166
x0, y0, z0 = 0, 1, 1.05

# Assigns $t$ as a set of $n$ evenly spaced points from 0 to tmax
tmax, n = 100, 10000
t = np.linspace(0, tmax, n)


def lorenz(t, V, sigma, b, r):
    """The Lorenz equations."""
    x, y, z = V
    xp = sigma*y - sigma*x
    yp = r*x - y - x*z
    zp = x*y-b*z
    return xp, yp, zp


# Integrate the Lorenz equations. This is the 3d version of the numerical
# solver used in PENDULUM.
soln = solve_ivp(lorenz, (0, tmax), (x0, y0, z0), args=(sigma, b, r),
                 dense_output=True)

# Plots the solution along the time points we chose earlier
# Uses interpolation to smooth out the curve
x, y, z = soln.sol(t)

# Plot the Lorenz attractor using a Matplotlib 3D projection.
fig = plt.figure(facecolor='k', figsize=(WIDTH/DPI, HEIGHT/DPI))
ax = fig.gca(projection='3d')
ax.set_facecolor('k')
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

# Make the line multi-coloured by plotting it in segments of length s which
# change in colour across the whole time series.
s = 10
cmap = plt.cm.winter
for i in range(0, n-s, s):
    ax.plot(x[i:i+s+1], y[i:i+s+1], z[i:i+s+1], color=cmap(i/n), alpha=0.4)

# Remove all the axis clutter, leaving just the curve.
ax.set_axis_off()

plt.show()
