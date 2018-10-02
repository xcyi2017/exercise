def bubleSort(nums):
	for i in range(len(nums) - 1):
		for j in range(len(nums)-i-1):
			if nums[j] < nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
	return nums

nums = [5,2,45,6,8,2,1]
print(bubleSort(nums.copy()))

list1 = [3*x for x in nums]
print(list1)
del list1[0]
print(list1)
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)

print(knights.items())

for i, v in enumerate(['tic', 'tac', 'toe'], 1):
	print(i,v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your{}?  It is {}'.format(q, a))

for i in reversed(range(9)):
	print(i)