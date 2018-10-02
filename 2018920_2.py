import numpy as np
import matplotlib.pyplot as plt

initialT = 1000
alpha = 0.99
k = 1
endT = 0.01
maxIter = 200


currentT = initialT
eta =0.01
theta = np.random.uniform(-1,2)
last_x = [theta]

def J(x):
    return x*np.sin(10*np.pi*x)+2

def dJ(x):
    return (J(x+1e-5)-J(x))/(1e-5)

while currentT > endT:
    for t in range(maxIter):
        theta_new = theta+np.random.uniform(-0.5,0.5)
        if -1<=theta_new and theta_new<=2:
            res = J(theta_new)-J(theta)
            if res<0:
                theta = theta_new
                last_x.append(theta)
            else:
                if np.random.rand()<np.exp(-(res)/(currentT)):
                    theta = theta_new
                    

    currentT = alpha*currentT

print('最优值',J(np.array(last_x[-1])))
x = np.linspace(-1,2,1000)
y = J(x)
plt.figure()
plt.plot(x,y)
plt.scatter(np.array(last_x[:-1]),J(np.array(last_x[:-1])),marker='+')
plt.scatter(np.array(last_x[-1]),J(np.array(last_x[-1])),marker='o')
plt.show()


    
        
