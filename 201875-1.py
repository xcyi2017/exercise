import numpy as np
import matplotlib.pyplot as plt


def fun(X):
    return X + X*np.exp(np.cos(X))



xx = np.linspace(-10, 10, 1000)
yy = fun(xx)

plt.figure()
plt.plot(xx,yy)

currentx = np.random.uniform(-10,10)
plt.plot(currentx, fun(currentx), 'o')


currentT = 1000
k = 1
mint = 1
max_iter = 1000
alpha = 0.99

while currentT > mint:
    for i in range(max_iter):
        newx = currentx + np.random.uniform(-1,1)
        if newx>=-10 and newx<=10:
            res = fun(newx) - fun(currentx)
            if res < 0:
                currentx = newx
            else:
                if np.random.rand() < np.exp(-(res)/(k*currentT)):
                    currentx = newx
                
    currentT = alpha*currentT


plt.plot(currentx, fun(currentx), '*')
plt.show()