def solve(h, l):
    for x in range(h+1):
        th = x
        jt = h - x
        if th*4+jt*2 == l:
            print('鸡：{0}\n兔：{1}'.format(th, jt))

solve(20, 70)