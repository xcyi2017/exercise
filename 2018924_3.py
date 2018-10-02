import numpy as np
import random
import matplotlib.pyplot as plt

class tsp:
    def __init__(self, count,):
        self.count = count
        self.population = self.gen_population(count)
        self.dic = dict(zip(['A','B','C','D','E','F','G','H'], list(range(8))))
        self.dis = np.loadtxt('../data.csv', delimiter=',')
        pass
    
    def gen_chromosome(self):
        str1 =  ['B','C','D','E','F','G']
        random.shuffle(str1)
        return  np.array(['A']+ str1 + ['H'])

    def gen_population(self, count):
        return [self.gen_chromosome() for _ in range(count)]

    def selection(self, retain_rate, random_rate):
        graded = [(self.fitness(chromosome), chromosome) for chromosome in self.population]
        graded = [x[1] for x in sorted(graded,key= lambda x: x[0])]
        retain_len = int(len(graded)*retain_rate)
        parents = graded[:retain_len]
        for chromosome in graded[retain_len:]:
            if np.random.rand() < random_rate:
                parents.append(chromosome)
        return parents
    
    def crossover(self, parents):
        children = []
        target_length = int(len(self.population)-len(parents))
        while len(children) < target_length:
            male = np.random.randint(0, len(parents))
            female = np.random.randint(0, len(parents))

            if male != female:
                male = parents[male]
                female = parents[female]
                father_point = np.array([1 if x%2==0 else 0 for x in range(0,8)], dtype=np.bool)
                father_city1 = male[father_point]
                father_city2 = male[np.invert(father_point)]
                mother_point = np.isin(female, father_city2)
                mother_city = female[mother_point]
                child = np.r_[father_city1, mother_city]
                children.append(child)
                # print(child)
        self.population = parents + children

    def mulation(self, rate):
        for i in range(len(self.population)):
            if np.random.rand() < rate:
                j, k = np.random.permutation(range(1,7))[:2]
                self.population[i][j], self.population[i][k] = self.population[i][k],self.population[i][j]

    def fitness(self, chromosome):
        index = [(self.dic[i], self.dic[j]) for i,j  in zip(chromosome[:-1], chromosome[1:])]
        return np.sum([self.dis[ind] for ind in index])

    def solve(self,  retain_rate, random_rate, mulation_rate, n_iters):
        cur_iter = 0
        iter_fit = []
        while cur_iter < n_iters:
            parents = self.selection(retain_rate, random_rate)
            self.crossover(parents)
            self.mulation(mulation_rate)
            ts = 1e10
            for s in self.population:
                ss = float(self.fitness(s))
                if ss<ts:
                    ts = ss
            iter_fit.append(ts)
            cur_iter += 1
        return iter_fit
    

if __name__ == '__main__':
    ts = tsp(count=50)
    fit = ts.solve(retain_rate=0.2, random_rate=0.75, mulation_rate=0.01,n_iters=200)
    plt.figure()
    plt.plot(fit)
    plt.xlabel('iter')
    plt.ylabel('fitness')
    plt.title('TSP using GA')
    plt.tight_layout()
    plt.show()