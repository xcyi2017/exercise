import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
x = np.arange(-4,4,0.25)
y = np.arange(-4,4,0.25)
x, y = np.meshgrid(x, y)
z = x**2 +y**2 +np.sin(x*y)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')

plt.show()