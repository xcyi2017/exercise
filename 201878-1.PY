import numpy as np
import matplotlib.pyplot as plt
import random


class GA():

    def __init__(self, length, count):
        self.length = length
        self.count = count
        self.population = self.gen_population(count, length)


    def fun(self, chromosome):
        x  = self.decode(chromosome)
        return x + 10*np.sin(5*x) + 7*np.cos(4*x)


    def gen_chromosome(self, length):
        chromosome = 0
        for i in range(length):
            chromosome |= (1<<i)*np.random.randint(0,2)
        return chromosome

    def gen_population(self, count, length):
        return [self.gen_chromosome(length) for i in range(count)]

    def collection(self, retain_rate, random_rate):
        graded = [(self.fun(chromosome), chromosome) for chromosome in self.population]
        graded = [x[1] for x in sorted(graded, reverse =True)]
        retain_length = int(self.length*retain_rate)
        parents = graded[:retain_length]
        for i in graded[retain_length:]:
            if np.random.rand() < random_rate:
                parents.append(i)
        return parents, self.fun(graded[0])

    def crossover(self, parents):
        children = []
        while len(children) < (self.count - len(parents)):
            male = np.random.randint(0, len(parents))
            female = np.random.randint(0, len(parents))
            if male != female:
                mask = 0
                cross_pos = random.randint(0, self.length)
                for i in range(cross_pos):
                    mask |= 1<<i
                male = parents[male]
                female = parents[female]
                child = ((male&mask)|(female&~mask)) & ((1<<self.length)-1)
                children.append(child)
        self.population = parents + children

    def multation(self, rate):
        for i in range(self.count):
            if np.random.rand() < rate:
                j = random.randint(0,self.length-1)
                self.population[i] ^= 1<<j
    
    def decode(self, chromosome):
        return chromosome *(9/(2**self.length -1))

class SA():

    def __init__(self, init_x= random.uniform(0,9), init_t =1000, k=1, max_iter=200, alpha=0.99, end_t=1e-6):
        self.init_x = init_x
        self.init_t = init_t
        self.k = k 
        self.max_iter = max_iter
        self.alpha = alpha
        self.end_t = end_t
    
    def fun(self, x):
        return x + 10*np.sin(5*x) + 7*np.cos(4*x)
    def ts(self):
        fitness = []
        while self.init_t > self.end_t:
            for i in range(self.max_iter):
                xnew = self.init_x + random.uniform(-0.5, 0.5)
                if xnew>= 0 and xnew<=9:
                    res = self.fun(xnew) - self.fun(self.init_x)
                    if res > 0:
                        self.init_x = xnew
                    else:
                        if np.random.rand() < np.exp(res/(self.k*self.init_t)):
                            self.init_x = xnew
                    fitness.append(self.fun(self.init_x))
            self.init_t = self.alpha * self.init_t

        return fitness


if __name__ == '__main__':
    ga = GA(length=17, count=300)
    fitness = []
    for i in range(20):
        parents, bestfitness = ga.collection(retain_rate=0.2,random_rate=0.5)
        fitness.append(bestfitness)
        ga.crossover(parents)
        ga.multation(rate=0.01)

    sa = SA()
    sa.ts()
    
    fig = plt.figure() 
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    x = np.linspace(0,9,1000)
    y = x + 10*np.sin(5*x) + 7*np.cos(4*x)
    ax1.plot(x,y)
    xx = ga.decode(parents[0])
    yy = bestfitness
    ax1.plot(xx,yy,'o')
    ax1.plot(sa.init_x,sa.fun(sa.init_x),'*')
    ax2.plot(fitness)
    plt.tight_layout()
    plt.show()