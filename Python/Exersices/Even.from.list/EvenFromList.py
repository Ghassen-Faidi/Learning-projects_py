nums = [21, 12, 2, 35, 6, 96, 9, 41, 72, 17, 3, 88]
even_nums = []

for i in range(len(nums)):
	if (nums[i] % 2 ) == 0:
		even_nums.append(nums[i])
		
print(f"the even numbers are:\n{even_nums}")