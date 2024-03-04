# JULIA plots the Julia set for gc(z) = z^2 + c
import numpy as np
import matplotlib.pyplot as plt


# Change the values for c here. You may also adjust the number iter of iterates
# The number of evenly spaced points on the complex axes N
# for the bounds on the complex plane X0.
def julia_set(
    c=-0.70176 - 0.3842 * 1j, num_iter=50, N=1000, X0=np.array([-2, 2, -2, 2])
):

    # Defines the limits of the complex grid.
    x0 = X0[0]
    x1 = X0[1]
    y0 = X0[2]
    y1 = X0[3]

    # This makes a grid array for the x and y values, and combines then into
    # a grid z of complex numbers.
    x, y = np.meshgrid(np.linspace(x0, x1, N), np.linspace(y0, y1, N) * 1j)
    z = x + y
    # F keeps track of which grid points are bounded
    # even after many iterations of z = z ∗ ∗2 + c.
    # This is done by making an N × N array of zeros
    # and iterating our function. For each entry in the array z, if the absolute
    # value of z is finite, the corresponding entry in F is increased by 1.
    # These values are used to produce the colors in the eventual image.
    F = np.zeros([N, N])
    # Iterate through the operation z := z**2 + c.
    for j in range(num_iter):
        z = z**2 + c
        index = np.abs(z) < np.inf
        F[index] = F[index] + 1
    return np.linspace(x0, x1, N), np.linspace(y0, y1, N), F


x, y, F = julia_set(
    c=-0.835 - 0.2421 * 1j, num_iter=100, N=1000, X0=np.array([-1.5, 1.5, -1.5, 1.5])
)

plt.figure(figsize=(10, 10))
plt.pcolormesh(x, y, F, cmap="twilight_shifted")
plt.axis("equal")
plt.axis("off")
plt.savefig("JuliaCover.png")

plt.show()
