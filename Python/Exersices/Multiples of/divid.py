div = int(input("get all multiples of: "))
max = int(input("set max: "))

for i in range(max):
	if i % div == 0:
		print(i)