import numpy as np
import random
import math
import matplotlib.pyplot as plt

class Smart:
    def __init__(self, max_iter, pN, dim):
        self.max_iter = max_iter
        self.pN = pN
        self.dim = dim
    def fun(self, X):
        return 1+10*np.sin(5*X) + 7*np.cos(4*X)
    
    def plot_(self, DATA):
        plt.figure()
        plt.plot(DATA)
        plt.tight_layout()
        plt.show()


class PSO(Smart):
    def __init__(self, max_iter, pN, dim):
        self.w = 0.8
        self.c1 = 2
        self.c2 = 2
        Smart.__init__(self, max_iter, pN, dim)
        self.V = np.zeros((self.pN, self.dim))
        self.X = np.zeros((self.pN, self.dim))
        self.pbest = np.zeros((self.pN, self.dim))
        self.gbest = np.zeros((1, self.dim))
        self.p_fit = np.zeros(self.pN)
        self.fit = 1e-10
    def init_(self):
        for i in range(self.pN):
            for j in range(self.dim):
                self.V[i][j] = random.uniform(0,1)
                self.X[i][j] = random.uniform(0,1)
            self.pbest[i] = self.X[i]
            temp = self.fun(self.X[i])
            self.p_fit[i] = temp
            if temp > self.fit:
                self.fit = temp
                self.gbest = self.X[i] 
    def process(self):
        fitness = []
        for t in range(self.max_iter):
            for i in range(self.pN):
                temp = self.fun(self.X[i])
                if temp > self.p_fit[i]:
                    self.p_fit[i] = temp
                    self.pbest[i] = self.X[i]
                    if self.p_fit[i] > self.fit:
                        self.fit = self.p_fit[i]
                        self.gbest = self.X[i]
            for i in range(self.pN):
                self.V[i] = self.w*self.V[i] + self.c1*random.random()*(self.pbest[i]-self.X[i]) + self.c2*random.random()*(self.gbest - self.X[i])
                self.X[i] = self.X[i] + self.V[i]
            fitness.append(self.fit)
        return fitness
    
class GA(Smart):
    def __init__(self, max_iter, pN, dim):
         Smart.__init__(self, max_iter, pN, dim)
         self.population = self.gen_population()

    def gen_chromosome(self, dim):
        chromosome = 0
        for i in range(dim):
            chromosome |= (1<<i) * random.randint(0, 1)
        return chromosome

    def gen_population(self):
        return [self.gen_chromosome(self.dim) for i in range(self.pN)]
    
    def decode(self, chromosome):
        return chromosome * 9 /(2**self.dim - 1)

    def selection(self, retain_rate, random_rate):
        graded = [(self.fun(chromosome), chromosome) for chromosome in self.population]
        graded = [x[1] for x in sorted(graded, reverse = True)]
        retain_length = int(self.dim*retain_rate)
        parents = graded[:retain_length]
        for chromosome in graded[retain_length:]:
            if random.random() < random_rate:
                parents.append(chromosome)
        return parents

    def crossover(self, parents):
        children = []
        temp = self.pN - len(parents)
        while len(children) < temp:
            male = random.randint(0, len(parents)-1)
            female = random.randint(0, len(parents)-1)
            if male != female:
                mask = 0
                cross_pos = random.randint(0,self.dim)
                for i in range(cross_pos):
                    mask |= (1<<i)
                male = parents[male]
                female = parents[female]
                child = ((male & mask) | (female & ~mask)) & ((1 << self.dim) - 1)
                children.append(child)
                self.population = parents + children

    def mutation(self, rate):
        for i in range(self.pN):
            if random.random() < rate:
                j = random.randint(0,self.dim-1)
                self.population[i] ^= 1<<j

    
    def evolve(self, retain_rate=0.2, random_rate=0.5, mutation_rate=0.01):
        gbest = []
        for x in range(self.max_iter):
            parents = self.selection(retain_rate, random_rate)
            self.crossover(parents)
            self.mutation(mutation_rate)
            gbest.append(sorted([self.fun(x) for x in self.population],reverse=True)[0])
        return gbest
    

    
if __name__ == '__main__':
    pso = PSO(max_iter=200, pN=30, dim = 1)
    pso.init_()
    fitness = pso.process()
    ga = GA(max_iter=200, pN=50, dim=17)
    gbest = ga.evolve()
    fig = plt.figure()
    ax1 = fig.add_subplot(2,1,1)
    ax1.plot(fitness)
    ax1.set_xlabel('iter')
    ax2 = fig.add_subplot(2,1,2)
    ax2.plot(gbest)
    plt.tight_layout()
    plt.show()
