import numpy as np
def binary_sort(lists, item):
	low = 0
	high = len(lists) - 1

	while low <= high:
		mid = int((low + high) / 2)
		guess = lists[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

my_list = range(100000000000)
print(binary_sort(my_list, 1000))
