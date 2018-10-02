import numpy as np

arr = [1, 2, 4, 1, 7, 8, 3]
arr1 = [3, 34, 4, 12, 5, 2]
def rec_opt(arr, i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    else:
        A = rec_opt(arr, i-2) + arr[i]
        B = rec_opt(arr, i-1)
    return max(A,B)

print(rec_opt(arr,6))

def dp_opt(arr):
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2,len(arr)):
        A = opt[i-2] + arr[i]
        B = opt[i-1]
        opt[i] = max(A,B)
    return opt[len(arr) - 1]
print(dp_opt(arr))

def rec_subset(arr1, i, s):
    if s == 0:
        return True
    elif i == 0:
        return arr1[0] == s
    elif arr1[i] > s:
        return rec_subset(arr1, i-1, s)
    else:
        A = rec_subset(arr1,i-1,s- arr1[i])
        B = rec_subset(arr1,i-1,s)
        return A or B
print(rec_subset(arr1,len(arr1)-1,9))

def dp_subset(arr1, s):
    subset = np.zeros((len(arr1), s+1), dtype=bool)
    subset[:,0] = True
    subset[0,:] = False
    subset[0,arr[0]] = True
    for i in range(1,len(arr1)):
        for s in range(1, s+1):
            if arr1[i] > s:
                subset[i,s] = subset[i-1,s]
            else:
                A = subset[i-1,s-arr1[i]]
                B = subset[i-1,s]
                subset[i,s] = A or B
    r, c = subset.shape
    return subset[r-1,c-1]

print(dp_subset(arr1,9))