import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 1, 100)
b = np.linspace(-1, 0, 100)

c = 0.01

A, B = np.meshgrid(a, b)

eta_s = (-B + np.sqrt(B**2 - 4*A*c)) / (2*c)

plt.pcolormesh(A, B, eta_s, cmap='viridis')
plt.colorbar()
plt.xlabel('a')
plt.ylabel('b')
plt.show()
print('here')