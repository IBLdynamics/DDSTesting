

''' A function to determine the values of the Julia set. Takes
	an array size specified by h_range and w_range, in pixels, along
	with the number of maximum iterations to try.  Returns an array with
	the number of the last bounded iteration at each array value.
	'''

import numpy as np
import matplotlib.pyplot as plt

c = -0.744 + 0.148j


def julia(h_range, w_range, max_iterations):
    y, x = np.ogrid[1.4: -1.4: h_range*1j, -
                    1.4: 1.4: w_range*1j]  # top left to bottom right
    z_array = x + y*1j

    iterations_till_divergence = max_iterations + np.zeros(z_array.shape)

    for h in range(h_range):
        for w in range(w_range):
            z = z_array[h][w]
            for i in range(max_iterations):
                z = z**2 + c
                if z * np.conj(z) > 4:
                    iterations_till_divergence[h][w] = i
                    break

    return iterations_till_divergence


plt.imshow(julia(500, 500, 70), cmap='twilight_shifted')
plt.axis('off')
plt.show()
