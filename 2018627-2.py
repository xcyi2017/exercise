def proc(arg):
    sum = 0
    for i in arg:
        sum += eval(i)**2
    return sum


n = 1000#循环次数

a = input('输入数字：')
b = eval(a)
while True:
    b = proc(str(b))
    n -= 1
    if b == 1:
        print('True')
        break
    elif n == 0:
        print('Flase')
        break

