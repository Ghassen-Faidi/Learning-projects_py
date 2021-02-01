num = int(input("Type an integer: "))
divs = []

for i in range(1, num+1):
	if num % i == 0: 
		divs.append(i)

if len(divs) == 2: # the 2 items are the number and 1
		print(f"{num} is prime")
else:
	print(f"{num} is not prime")