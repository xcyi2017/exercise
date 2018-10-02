import numpy as np
import pandas as pd

tup = tuple(['foo', [1, 3], True])
tup[1].append(3)
a, (b1, b2, b3), c = tup
print(a, b1, b2, b3, c)
seq = [(1,2,3),(4,5,6),(7,8,9)]
for a, b, c in seq:
	print('a={0},b={1},c={2}'.format(a,b,c))

values = 1, 2, 3, 4, 5
a, b, *rest = values
print(a,b, rest)
aa = (1, 2, 2, 2, 3, 4, 2)
print(aa.count(2))
bb = [7, 2, 5, 1, 3]
bb.sort(reverse = True)
print(bb)
cc = [i for i in 'python']
print(cc)
dd = 'I love python'
dd1 = dd.split()
print(dd1)
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'],index=['a', 'd', 'c', 'd'])
print(string_data.isnull())

