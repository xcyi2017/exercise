import matplotlib.pyplot as plt
import numpy as np
class A:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def run(self):
        print('Hello world!')

    def plot_(self, x, y):
        plt.figure()
        plt.plot(x, y)
        plt.show()



class B(A):

    def __init__(self, name, score):
        super(B, self).__init__(name, score)
        

    def run1(self):
        print(self.name, self.score)

    def run2(self):
        self.run()
    
    def run3(self):
        x = np.linspace(0,9,10000)
        y = x+10*np.sin(5*x) + 7*np.cos(4*x)
        self.plot_(x, y)

if __name__  == '__main__':
    C = B('xu', 90)
    C.run()
    C.run1()
    C.run2()
    C.run3()
    