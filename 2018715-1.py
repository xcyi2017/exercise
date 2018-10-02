"""
 一. 使用匿名函数对1~1000求和，代码力求简洁。
"""
# from functools import reduce
# a = reduce((lambda x,y:x+y),range(1,1001))
# print(a)
# i = 0
# while i<=7:
#     i += 1
#     if i<=4:
#         print('{0:^{1}}'.format('*'*(2*i-1),7))
#     else:
#         print('{0:^{1}}'.format('*'*(-2*i+15),7))

'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。
'''
# import numpy as np
# frac_a = np.zeros(20)
# frac_b = np.zeros(20)
# frac_b[:2]=[2,3]
# frac_a[:2]=[1,2]
# for i in range(2,20):
#     frac_a[i] = frac_a[i-1] + frac_a[i-2]
#     frac_b[i] = frac_b[i-1] + frac_b[i-2]
# print(sum(frac_b/frac_a))

'''
题目：求1+2!+3!+…+20!的和。
'''
# def A_n(n):
#     an = 1
#     for i in range(1,n+1):
#         an *= i
#     return an

# def sum_an(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += A_n(i)
#     return sum

# print(sum_an(20))

'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
# def get_num(n):
#     num = str(n)
#     print('{}位数'.format(len(num)))
#     print(num[::-1])
# get_num(2345)

'''
有一群人站队，每人通过一对整数(h, k)来描述，其中h表示人的高度，k表示在此人前面队列中身高不小于此人的总人数。

实现一个算法输出这个队列的正确顺序。

输入：

[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
输出：

[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''
from operator import itemgetter
queue = eval(input())

queue.sort(key = itemgetter(1))
print(queue)
queue.sort(key = itemgetter(0), reverse = True)
print(queue)

output = []
for item in queue:
    print(item)
    output.insert(item[1], item)
print(output)