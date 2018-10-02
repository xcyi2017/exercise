import numpy as np
import random
import matplotlib.pyplot as plt
from math import pi, sin

class PSO():

    def __init__(self, pN, max_iter, dim):
        self.w = 0.8 #惯性因子
        self.c1 = 2
        self.c2 = 2
        self.pN = pN #粒子个数 
        self.max_iter = max_iter  #迭代次数
        self.dim = dim #搜索维度
        self.X_bound = [-1, 2]
        self.V = np.zeros((self.pN, self.dim))#记录粒子的速度
        self.X = np.zeros((self.pN, self.dim))#记录粒子的位置
        self.pbest = np.zeros((self.pN, self.dim))#记录粒子最佳位置
        self.gbest = np.zeros((1, self.dim))#记录迭代过程中全局最佳位置
        self.p_fit = np.zeros(self.pN)#记录每个粒子历史的最优值
        self.fit = 1e10 #全局最佳适应值

    def init(self):
        for i in range(self.pN):
            for j in range(self.dim):
                self.V[i][j] = random.uniform(0, 1)
                self.X[i][j] = random.uniform(self.X_bound[0], self.X_bound[1])
            self.pbest[i] = self.X[i]
            tmp = self.fun(self.X[i])
            self.p_fit[i] = tmp
            if tmp < self.fit:
                self.fit = tmp
                self.gbest = self.X[i]


    def fun(self, arg):
        return np.sum(np.square(arg)) + 1
    

    def process(self):
        fitness = []
        for j in range(self.max_iter):
            for i in range(self.pN):
                tmp = self.fun(self.X[i])#计算出的适应度值
                if tmp < self.p_fit[i]:
                    self.p_fit[i] = tmp#更新粒子的最优值
                    self.pbest[i] = self.X[i]#更新
                    if self.p_fit[i] < self.fit:
                       self.gbest = self.X[i]
                       self.fit = self.p_fit[i]
            for i in range(self.pN):
                self.V[i] = self.w * self.V[i] + self.c1 * random.random() * (self.pbest[i] - self.X[i]) +self.c2 * random.random() * (self.gbest - self.X[i])
                self.X[i] = self.X[i] + self.V[i]
                # for j in range(self.dim):
                #     if self.X[i][j] > 2 or self.X[i][j] < -1:
                #         continue
            print(self.fit)
            fitness.append(self.fit)  
        return fitness   
                


    def save_and_plot(self, data):
        plt.figure()
        plt.plot(data)
        plt.title('Fitness')
        plt.ylabel('fitness')
        plt.xlabel('intern')
        plt.show()
        

if __name__ == '__main__':
    pso = PSO(pN=30,dim=3,max_iter=200)
    pso.init()
    fitness = pso.process()
    print(fitness)
    pso.save_and_plot(fitness)