my_list = list(range(1,31))
out_list = []
x = 0
i = 0
while len(out_list) < 15:
    if x > 29:
        x = 0
    if my_list[x] not in out_list:
        i = i+1
    if i == 9:
        print('{:2d} {}'.format(my_list[x], '出列'))
        out_list.append(my_list[x])
        i = 0
    x += 1

        
