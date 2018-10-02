def jc(arg):
    tt = 1
    for i in range(1, arg+1):
        tt *= i
    return tt

def Sum(arg):
    sum = 0
    for i in range(1, arg+1):
        sum += jc(i)
    return sum


a = input('请输入数字：')
try:
    b = eval(a)
except NameError:
    print('输入有误，请输入正整数')
else:
    if type(b) == int:
        obj = Sum(b)
        print(obj)
    else:
        print('输入有误，请输入正整数')