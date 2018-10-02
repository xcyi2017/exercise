import numpy as np
import matplotlib.pyplot as plt


class PSO():


    def __init__(self, pN, max_iter, dim):
        self.w = 0.8
        self.c1 = 2
        self.c2 = 2
        self.pN = pN
        self.max_iter =max_iter
        self.dim = dim
        self.X = np.zeros((self.pN, self.dim))
        self.V = np.zeros((self.pN, self.dim))
        self.pbest = np.zeros((self.pN, self.dim))
        self.gebest = np.zeros((1, self.dim))
        self.p_fit = np.zeros(self.pN)
        self.fit = 1e10

    def fun(self, X):
        return X + X**2



    def init_(self):
        for i in range(self.pN):
            for j in range(self.dim):
                self.X[i][j] = np.random.uniform(0,9)
                self.V[i][j] = np.random.uniform(0,1)
            temp = self.fun(self.X[i])
            self.pbest[i] = temp
            if temp < self.fit:
                self.fit = temp
                self.gbest = self.X[i]

    def process(self):
        fitness = []
        for t in range(self.max_iter):
            for i in range(self.pN):
                temp = self.fun(self.X[i])
                if temp < self.p_fit[i]:
                    self.p_fit[i] = temp
                    self.pbest[i] = self.X[i]
                    if self.p_fit[i] < self.fit:
                        self.fit = self.p_fit[i]
                        self.gbest = self.X[i]
            for i in range(self.pN):
                self.V[i] = self.w*self.V[i] + self.c1*np.random.rand()*(self.pbest[i] - self.X[i]) + self.c2*np.random.rand()*(self.gbest - self.X[i])
                self.X[i] = self.X[i] + self.V[i]
            fitness.append(self.fit)
        return fitness


pso = PSO(pN=30,max_iter=200,dim=1)
pso.init_()
fitness = pso.process()
plt.figure()
plt.plot(fitness)
plt.show()