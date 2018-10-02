import numpy as np
import time
from sklearn import datasets


class Network:
    def __init__(self, sizes, eta=3):
        self.eta = eta
        np.random.seed(1)
        self.layers = len(sizes)
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights =[np.random.randn(y,x) for x, y in zip(sizes[:-1], sizes[1:])]
        pass


    def sigmoid(self, x):
        return 1/(1+np.exp(-x))


    def sigmoid_prime(self, x):
        return self.sigmoid(x)*(1-self.sigmoid(x))

    def backdrop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        activation = x
        activations = [x]
        zs =[]
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = self.sigmoid(z)
            activations.append(activation)
        delta = (activations[-1]-y)*self.sigmoid_prime(zs[-1])

        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())

        for l in range(2,self.layers):
            z = zs[-l]
            delta = np.dot(self.weights[-l+1].transpose(), delta)*self.sigmoid_prime(z)

            nabla_b[-l] = delta

            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return nabla_b, nabla_w

    def fit(self, X, y):
        cur_iter = 0
        n_iter = 10000
        while cur_iter < n_iter:
            nabla_b = [np.zeros(b.shape) for b in self.biases]
            nabla_w = [np.zeros(w.shape) for w in self.weights]
            for xi, yi in zip(X, y):
                if np.random.randint(0,2):
                    delta_nabla_b, delta_nabla_w = self.backdrop(xi, yi)
                    nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
                    nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
            self.weights = [w-self.eta*(nw)/len(X) for w, nw in zip(self.weights, nabla_w)]
            self.biases = [b-self.eta*(nb)/len(X) for b, nb in zip(self.biases, nabla_b)]
            cur_iter += 1
        pass

    def feedforward(self, x):
        x = np.array(x).reshape(-1,1)
        for b, w in zip(self.biases, self.weights):
            x = self.sigmoid(np.dot(w, x) + b)
        return x

    def predict(self, x):
        test_results = self.feedforward(x)
        return test_results

if __name__ == '__main__':
    start = time.time()
    # X = np.array([[0,0],[0,1],[1,0],[1,1]])
    X = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    X = [x.reshape(-1,1) for x in X]
    # y = np.array([1,0,0,1])
    y = np.array([0, 0, 0, 0, 1, 1, 1])
    net = Network(sizes=[3,4,1])
    net.fit(X, y)
    print(net.weights,'\n', net.biases)
    for x in X:
        print(net.predict(x))
    end = time.time()
    print('运行时间：{}s'.format(end-start))