num = int(input("Type a number: "))

if num % 2 == 0:
	msg = "is even"
	# Extra exersice
	if num == 4:
		print("FOUR is even!")
else:
	msg = "is odd"

if num != 4:
	print(num, msg)