import numpy as np
import matplotlib.pyplot as plt


class PSO:

    def __init__(self,N,dim,n_iter):
        self.w = 0.8