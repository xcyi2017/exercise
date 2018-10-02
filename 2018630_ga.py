import matplotlib.pyplot as plt
import numpy as np
import math
import random

class GA():

    def __init__(self, length, count):
        '''
        length:染色体长度
        count：种群大小
        '''
        self.length = length
        self.count = count
        self.population = self.gen_populatin(length, count)
        

    
    def gen_chromosome(self, length):
        '''
        随机产生一个染色体
        '''
        chromosome = 0
        for i in range(length):
            chromosome |= (1<<i) * np.random.randint(0, 1)
        return chromosome


    def gen_populatin(self, length, count):
        '''
        随机产生种群
        '''
        return [self.gen_chromosome(length) for i in range(count)]

    
    def selection(self, retain_rate, random_select_rate):
        graded = [(self.fitness(chromosome), chromosome) for chromosome in self.population]
        graded = [x[1] for x in sorted(graded, reverse = True)]
        gbest = sorted(graded, reverse = True)[0]
        retain_length = int(len(graded) * retain_rate)
        parent = graded[:retain_length]
        for chromosome in graded[retain_length:]:
            if random.random() < random_select_rate:
                parent.append(chromosome)
        return parent, gbest


    def crossover(self, parent):
        children = []
        target_count = len(self.population) - len(parent)
        while target_count < len(children):
            male = random.randint(0, len(parent))
            female = random.randint(0, len(parent))
        if male != female:
            cross_pot = random.randint(0, self.length)
            mask = 0
            for i in range(cross_pot):
                mask |= (1<<i)
            male = parent[male]
            female = parent[female]
            child = (male & ~mask) | (female & mask) & ((1<<self.length)-1)
            children.append(child)
            self.population = parent + children
    
    def mutation(self, rate):
        for i in range(self.population):
            if random.random() < rate:
                j = random.randint(0, self.length)
                self.population[i] ^= (1<<j)

    def fitness(self, chromosome):
        x = self.decode(chromosome)
        return x + 10*math.sin(5*x) + 7*math.cos(4*x)


    def decode(self, chromosome):
        return chromosome*9.0/(2**self.length - 1)

    def evolve(self, retain_rate = 0.2, random_select_rate = 0.5, mutation_rate= 0.01):
        parent,gbest = self.selection(retain_rate, random_select_rate)
        self.crossover(parent)
        self.mutation(mutation_rate)
        return gbest


if __name__ == '__main__':
    ga = GA(17, 300)
    Gbest = []
    for x in range(200):
        gbest = ga.evolve()
        Gbest.append(gbest)
    plt.figure()
    plt.plot(Gbest)
    plt.show()


