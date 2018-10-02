from  random import random 
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np

proc = 1000
hist = 0

x = np.linspace(0, 2, 1000)
y = x ** 2
plt.plot(x, y)
plt.fill_between(x, y, where=(y > 0), color='red', alpha=0.5)


points = [[xy[0]*2,xy[1]*4] for xy in np.random.rand(proc, 2)]
plt.scatter([x[0] for x in points ],[y[1] for y in points], s=5, c=np.random.rand(proc), alpha=0.5)
plt.show()