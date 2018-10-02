from cvxpy import *
import pypower
x = Variable()
y = Variable()

constraints = [x+y==1,
               x-1>=1]

obj = Minimize(square(x-y))

prob = Problem(obj, constraints)
prob.solve()
print(prob.status)
print(prob.value)
print(x.value, y.value)