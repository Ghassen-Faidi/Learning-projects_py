list = [1, 3, 5, 8 ,96, 54, 0, 14, 23, 55, 12, 4]

less_than = []

x = int(input("Print all numbers less than: "))
for i in range (len(list)):
	num = list[i]
	if num < x:
		less_than.append(num)

print(less_than)