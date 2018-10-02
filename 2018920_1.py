import numpy as np
import matplotlib.pyplot as plt

def J(x):
    return x*np.sin(10*np.pi*x)+2


def dJ(x):
    return (J(x+1e-5)-J(x))/(1e-5)

def gradient(alpha=0.001):
    theta=np.random.uniform(-1,2)
    zs =[theta]
    while True:
        gradient = dJ(theta)
        last_theta = theta
        theta = theta - alpha*gradient
        zs.append(theta)
        if abs(dJ(last_theta)-dJ(theta))<1e-7:
            return zs

zs = gradient()
x = np.linspace(-1,2,1000)
y = J(x)
plt.figure()
plt.plot(x,y)
plt.plot(np.array(zs),J(np.array(zs)),'+')
plt.show()
