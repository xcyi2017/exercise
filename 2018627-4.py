a = input()

try:
    b  = eval(a)
except NameError:
    print('输入数据有误!')
except SyntaxError:
    print('输入数据有误!')
else:
    if b in range(101):
        if b>= 90:
            print('A\n祝贺你通过考试！')
        elif b>=80:
            print('B\n祝贺你通过考试！')
        elif b>=70:
            print('C\n祝贺你通过考试！')
        elif b>=60:
            print('D\n祝贺你通过考试！')
        else:
            print('E')
    else:
        print('输入数据有误!')
finally:
    print('好好学习，天天向上!')
