from time import time

start_time = time()
h = 35
l = 94
for  ch in range(0, h+1):
    rh = h - ch
    if ch * 2 + rh * 4 == l:
        print('c=%d'%ch)
        print('r=%d'%rh)
end_time = time()
print('Time cost:{}s'.format(end_time - start_time))