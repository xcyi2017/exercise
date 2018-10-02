import numpy as np
import math
import matplotlib.pyplot as plt
class GA:
    def __init__(self, length, count):
        self.length = length
        self.count = count
        self.population = self.gen_population(count, length)



    def gen_chromosome(self, length):
        """
        产生一个染色体
        """
        chromosome = 0
        for i in range(length):
            chromosome |= (1<<i)*np.random.randint(0,2)
        return chromosome
    
    def gen_population(self, count, length):
        """
        产生染色体组
        """
        return [self.gen_chromosome(length) for _ in range(count)]

    def selection(self, retain_rate, random_rate):
        """
        选择父代
        """
        graded = [(self.fitness(chromosome), chromosome) for chromosome in self.population]
        graded = [x[1] for x in sorted(graded, reverse=True)]
        retain_len = int(len(graded)*retain_rate)
        parents = graded[:retain_len]
        for chromosome in graded[retain_len:]:
            if np.random.rand()<random_rate:
                parents.append(chromosome)
        return parents

    def crossover(self, parents):
        """
        交叉产生子代
        """
        children = []
        target_length = (len(self.population)-len(parents))
        while len(children)<target_length:
            male = np.random.randint(0,len(parents))
            female = np.random.randint(0,len(parents))
            if male != female:
                cross_pos = np.random.randint(0, self.length)
                mask = 0
                for i in range(cross_pos):
                    mask |= (1<<i)
                male = parents[male]
                female = parents[female]
                child = (male & ~mask) | (female & mask)
                children.append(child)
        self.population = parents + children
        return self
    
    def mutation(self, rate):
        """
        随机选择变异
        """
        for i in range(self.count):
            if np.random.rand() < rate:
                j = np.random.randint(0, self.length)
                self.population[i] ^= (1<<j)
        return self

    def solve(self, count, length, retain_rate, random_rate, mutation_rate, n_iters):
        cur_iter = 0
        while cur_iter<n_iters:
            parents = self.selection(retain_rate, random_rate)
            self.crossover(parents)
            self.mutation(mutation_rate)
            cur_iter += 1


    def fitness(self, chromosome):
        x = self.decode(chromosome)
        return x + 10*math.sin(5*x) + 7*math.cos(4*x)

    def decode(self, chromosome):
        """
        对染色体进行解码
        """
        return chromosome*9.0/(2**self.length - 1)

if __name__ == '__main__':
    ga = GA(17, 30)
    ga.solve(count=17,length=300,retain_rate=0.2,random_rate=0.4, mutation_rate=0.01,n_iters=1000)
    for i in ga.population:
        print(ga.fitness(i))
    x = np.linspace(0,9, 1000)
    y = list(map(lambda xi: xi + 10*math.sin(5*xi) + 7*math.cos(4*xi), x))
    xx = [ga.decode(x) for x in ga.population]
    yy = [ga.fitness(x) for x in ga.population]
    plt.figure()
    plt.plot(x,y)
    plt.scatter(xx, yy, marker='+')
    plt.show()
    