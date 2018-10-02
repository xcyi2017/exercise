def findMin(arr):
	smallest = arr[0]
	small_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			small_index = i
	return small_index

def selectionSort(arr):
	arr1 = []
	for i in range(len(arr)):
		smallest_index = findMin(arr)
		arr1.append(arr.pop(smallest_index))
	return arr1

arr = [2,1,4,6,3,5]

print(selectionSort(arr))