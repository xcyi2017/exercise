from sklearn.neural_network import MLPClassifier

import numpy as np

X = [[0,0],[0,1],[1,0],[1,1]]
y = [1,0,0,1]

net = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(2,), random_state=6)
net.fit(X, y)
net.predict([0,0])