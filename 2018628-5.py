from itertools import product

def reverse(lis):
    list_ = []
    for j in lis:
        str = ''
        for i in j:
            if i == '0':
                str += '('
            elif i == '1':
                str += ')'
        list_.append(str)
    return list_


#对0-1字符串对称位取反
def cov(List):
    str = ''
    for i in List:
        if i == '1':
            str += '0'
        elif i == '0':
            str += '1'
    return str 

def rand(n):
    b = [''.join(x) for x in product(['0','1'], repeat = n)]
    c = list(map(lambda x: '0'+x+'1', b))
    c3 = []
    N = n + 2
    for i in c:
        li1 = i[:-int(N/2)]
        li2 = i[-int(N/2):]
        if li1 == cov(li2):
            c3.append(i) 
    return c3

def covert(arr):
    arr = arr[arr.index('0')+1:]
    if arr.find('0') + 1:
        

if __name__ == '__main__':
    n = 3
    str = rand(2*n-2)
    print(reverse(str))
    
