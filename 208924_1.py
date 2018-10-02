import numpy as np

class BP:

    def __init__(self, sizes):
        self.layers = len(sizes)
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    def feedForward(self,x):
        for w, b in zip(self.weights, self.biases):
            x = sigmoid(np.dot(w, x) + b)
        return x

    def backForward(self, x, y):
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        activation = x
        activations = [x]
        zs = []
        for w, b in zip(self.weights, self.biases):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        theta = (activations[-1] - y)*sigmoidPrime(zs[-1])
        nabla_w[-1] = np.dot(theta, activations[-2].transpose())
        nabla_b[-1] = theta
        for l in range(2,self.layers):
            theta = np.dot(self.weights[-l+1].transpose(), theta)*sigmoidPrime(zs[-l])
            nabla_b[-l] = theta
            nabla_w[-l] = np.dot(theta, activations[-l-1].transpose())
        return nabla_b, nabla_w

    
    def train(self, X, y):
        i_iter = 0
        n_iters = 20000
        alpha = 1
        while i_iter < n_iters:
            nabla_w = [np.zeros(w.shape) for w in self.weights]
            nabla_b = [np.zeros(b.shape) for b in self.biases]
            for xi, yi in zip(X, y):
                d_nabla_b, d_nabla_w = self.backForward(xi, yi)
                nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, d_nabla_b)]
                nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, d_nabla_w)]
            self.weights = [w - alpha*nw/len(X) for w, nw in zip(self.weights, nabla_w)]
            self.biases = [b -alpha*nb/len(X) for b, nb in zip(self.biases, nabla_b)]
            i_iter += 1

    def predict(self, x):
        return self.feedForward(x)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoidPrime(x):
    return sigmoid(x)*(1-sigmoid(x))
        

if __name__ == '__main__':
    X = np.array([[0,0,0],[0,0,1],[0,1,0],[1,0,0],[0,1,1],[1,0,1],[1,1,0],[1,1,1]])
    X = [x.reshape(-1,1) for x in X]
    y = np.array([0,0,0,0,1,1,1,1])
    bp = BP(sizes=[3,7,1])
    bp.train(X, y)
    for x in X:
        print(bp.predict(x))
