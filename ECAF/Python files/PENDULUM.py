# olves the equation for a damped pendulum
# You'll notice a new package here, scipy, which is needed for integration
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# Defining the system of differential equations
def system(xy, t, c, g, L, m):
    x = xy[0]
    y = xy[1]
    dx_dt = y
    dy_dt = -(c/(m*L))*y-g/L*np.sin(x)
    dtheta_dt = [dx_dt, dy_dt]

    return dtheta_dt


# Inputs
c = 0.05
g = 9.81
L = 1
m = 1

# initial condition
xy_0 = [0, 3]

# time plot
t = np.linspace(0, 20, 240)

# Solving ODE
theta = odeint(system, xy_0, t, args=(c, g, L, m))

plt.figure()
# Changes to $x$ ($\theta$) are in blue, changes to $y$ are in red.
plt.plot(t, theta[:, 0], 'b-')
plt.plot(t, theta[:, 1], 'r--')
plt.show()
