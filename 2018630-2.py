a = 0b110111010
b = 0b011101100
print(bin(a))
print(bin(b))
mask = 0
for i in range(5):
    mask |= (1<<i)

c = ((a&~mask) | (b&mask))
print(bin(c))