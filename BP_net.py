import numpy as np

def load_data():
    X = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    y = np.array([-1, -1, -1, -1, 1, 1, 1])
    return X, y

class BP_net:

    def __init__(self, eta=0.01, n_iter=100):
        self.eta = eta
        self.n_iter = n_iter
        np.random.seed(666)
        self.w = 2*np.random.random((4,1)) - 1
        
    
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))
    
    
    def fit(self, X_train, y_train):
        for _ in range(self.n_iter):
            z = np.dot(X, self.w[1:]) + self.w[0]
            alpha = self.sigmoid(z)
            update = self.eta*(y - alpha)*alpha*(1-alpha)
            self.w[1:] += update*X
            self.w[0] += update
        pass


    def predict(self, X_train):
        return self.sigmoid(np.dot(X_train, self.w[1:]) + self.w[0])
        pass


    def score(self, X_test, y_test):
        pass


if __name__ == '__main__':
    X, y = load_data()
    pre = BP_net()
    pre.fit(X, y)
    print(pre.predict(X))
