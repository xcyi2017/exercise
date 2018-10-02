from functools import reduce
from itertools import product

a = reduce(lambda x, y:[z0+z1 for z0 in x for z1 in y],[['0','1'],['0','1']], ['0', '1'])
print(a)

b = [''.join(x) for x in product(['0', '1'], repeat=2)]
print(b)
c = list(map(lambda x: '0'+ x +'1', b))
print(c)

c3 = []
for i in c:
    c1 = 0
    c2 = 0
    for j in i:
        if j=='1':
            c1 +=1
        elif j=='0':
            c2 += 1
    print(c1,c2)
    if c1==c2:
        c3.append(i) 
print(c3) 