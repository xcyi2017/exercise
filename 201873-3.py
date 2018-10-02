n = eval(input())

F = [0, 1]
while F[-1] < n:
   F.append(F[-1] + F[-2])
a = sum(F)
b = int(a/len(F))
F += a, b
C = [str(x) for x in F]
print(','.join(C))