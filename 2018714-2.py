from functools import reduce

'''
第一题：使用while循环输入 1 2 3 4 5 6     8 9 10
'''
# a = 0 
# while a<10:
#     a += 1
#     if a == 7:
#         continue
#     print(a)


'''
第二题：求1-100的所有数的和
'''
# sum = 0
# i = 0
# while i<100:
#     i += 1
#     sum += i
# print(sum)
    

'''
第三题：输出 1-100 内的所有奇数
'''
# js = []
# for i in range(1,101):
#     if i % 2 != 0:
#         js.append(i)
# print(js)


'''
功能要求：
要求用户输入自己拥有总资产，例如：2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
'''
# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998},
# ]
# whole_price = eval(input('请输入自己的总资产：'))
# items = {}
# price = {}
# for index, item in enumerate(goods):
#     items[index] = item['name']
#     price[index] = item['price']
# print(items)
# target_item = eval(input('请输入自己想买的物品编号：'))
# if whole_price < price[target_item]:
#     print('账户余额不足!')
# else:
#     print('购买成功!')



'''
题目：有1、2、3、4 个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''
# item_num = ['1', '2', '3', '4']

# a = reduce(lambda x,y:[z0+z1 for z0 in x for z1 in y],[item_num,item_num], item_num)
# b = [int(x) for x in a if x[0] != x[1] and x[0] != x[2] and x[1] != x[2]]
# print(b)

"""
题目：一个整数，它加上100 后是一个完全平方数，再加上168 又是一个完全平方数，请问该数是多少？
"""

# def num_12(num1, num2):
#     ans = abs(num1 - num2)
#     max_ys = []
#     for i in range(2,ans):
#         if ans % i == 0:
#             max_ys.append([i, int(ans/i)])
#     return [sorted(x) for x in max_ys]

# def solve():
#     list_ = num_12(168, 100)
#     for i in list_:
#         if (i[0] + i[1])%2 == 0 and (i[0]-i[1])%2 ==0:
#             return ((i[0]+i[1])/2)**2 - 168

# print(solve())

"""
题目：输出9*9 口诀表。
"""

for i in range(1,10):
    str1 = []
    for j in range(1,10):
        str1.append('{0}*{1}={2}'.format(i,j,int(i*j)))
    str1[:i-1] = ''
    print(str1)
