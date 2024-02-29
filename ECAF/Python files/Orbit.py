# ORBIT plots the orbit diagram of the quadratic family $Q_m$
# for m in [p,q].Attracting points are indicated by a solid line, and repelling by a dashed line
# Select the min value and max value of the window. The first coordinate is the value for $\mu$
# and the second for $x$.

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


fig, ax = plt.subplots(1, 1)
ax.set_title("Phase diagram for $Q_m(x) = mx(1-x)$", usetex='True')

x = np.linspace(0, 4, 100)
y = [0 for p in x]
ax.plot(x, y, color='black')
x = np.linspace(1, 4, 100)
y = [1 - 1/p for p in x]
ax.set_xlim(0, 4)
ax.set_ylim(-0.5, 1)
ax.plot(x, y, color='black')

v = np.linspace(-0.5, 1, 100)
lines = []
for i in range(1, 16):
    plt.plot(i*0.25*np.ones(100), v, color='black', alpha=0.25)
    plt.arrow(i*0.25, 0.85, 0, -0.1, shape='full', lw=2,
              length_includes_head=True, head_width=0.05, color='black')
    plt.arrow(i*0.25, -0.25, 0, -0.1, shape='full', lw=2,
              length_includes_head=True, head_width=0.05, color='black')
for i in range(5, 16):
    plt.arrow(i*0.25, 0.1, 0, 0.1, shape='full', lw=2,
              length_includes_head=True, head_width=0.05, color='black')

plt.xlabel('m')
plt.ylabel('x')
plt.show()
