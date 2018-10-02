def generate_a():
	for i in range(30):
		if i % 2 == 0:
			a = yield i
			print('a=',a+2)

b = generate_a()
print(b.__next__())
b.send(2)
b.__next__()