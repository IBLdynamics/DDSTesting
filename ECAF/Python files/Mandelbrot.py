# Import the modules we need for the program
# This code can run into some overflow warnings.
# These don't affect things we're interested in, so we ignore them
import matplotlib.pyplot as plt
import numpy as np


def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) < np.inf


x, y = np.meshgrid(np.linspace(-2, 0.5, 1000),
                   np.linspace(-1.5, 1.5, 1000) * 1j)
c = x + y
plt.imshow(is_stable(c, num_iterations=200), cmap="binary")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()
