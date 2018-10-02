import numpy as np
import matplotlib.pyplot as plt

class Pso():

    def __init__(self, pN, max_iter, dim):
        self.w = 0.8
        self.c1 = 2
        self.c2 = 2
        self.pN = pN
        self.max_iter = max_iter
        self.dim = dim
        self.V = np.zeros((self.pN, self.dim))
        self.X = np.zeros((self.pN, self.dim))
        self.pbest = np.zeros((self.pN, self.dim))
        self.gbest = np.zeros((1, self.dim))
        self.p_fit = np.zeros(self.pN)
        self.fit = 1e10


    def init_(self):
        for i in range(self.pN):
            for j in range(self.dim):
                self.V[i,j] = np.random.uniform(0, 1)
                self.X[i,j] = np.random.uniform(0, 1)
            self.pbest[i] = self.X[i,:]
            temp = fun(self.X[i,:])
            self.p_fit[i] = temp
            if temp < self.fit:
                self.fit = temp
                self.gbest = self.X[i]

    def iter(self):
        fitness = []
        for t in range(self.max_iter):
            for i in range(self.pN):
                temp = fun(self.X[i])
                if temp < self.p_fit[i]:
                    self.p_fit[i] = temp
                    self.pbest[i] = self.X[i]
                    if self.p_fit[i] < self.fit:
                        self.fit = self.p_fit[i]
                        self.gbest = self.X[i]
            for i in range(self.pN):
                self.V[i] = self.w*self.V[i] + self.c1*np.random.rand()*(self.pbest[i]-self.X[i])+self.c2*np.random.rand()*(self.gbest-self.X[i])
                self.V[i] = self.X[i] + self.V[i]
                self.V[i] = np.where(self.V[i]<=1,self.V[i], 1)
                self.X[i] = np.where(self.V[i]>=-1,self.V[i],-1)
                self.X[i] = np.where(self.X[i]<=2,self.X[i], 2)
                self.X[i] = np.where(self.X[i]>=-1,self.X[i],-1)
            fitness.append(self.fit)
        return fitness

    def plot(self, data):
        plt.figure()
        plt.plot(data)
        plt.show()


def fun(x):
        return x*np.sin(10*np.pi*x) + 2


if __name__ == '__main__':
    x = np.linspace(-1,2,1000)
    y = fun(x)
    pso = Pso(pN=20,dim=1,max_iter=200)
    pso.init_()
    fitness = pso.iter()
    plt.plot(x,y)
    plt.scatter(pso.p_fit[-1], fun(pso.p_fit[-1]),marker='^')
    pso.plot(fitness)
    plt.show()




