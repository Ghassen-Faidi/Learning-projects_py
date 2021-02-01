# Get an integer
num = int(input("Type a number: ")) 
# Get a divider
div = int(input(f" check if {num} is divisible by?: "))

if num % div == 0:  # check the reste
	print(f"{num}: is divisible by {div}")
else:
	print(f"{num}: isn't divisible by {div}")