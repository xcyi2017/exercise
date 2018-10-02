import numpy as np
import matplotlib.pyplot as plt

def fun(X):
    return (X-2)*(X+3)*(X+8)*(X-9)

xx = np.linspace(-10,10,300)
yy = fun(xx)
initx = 10*(2*np.random.rand()-1)
plt.figure()
plt.plot(xx, yy)
plt.plot(initx,fun(initx), 'o')
plt.show()