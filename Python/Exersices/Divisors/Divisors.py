num = int(input("Type a number: "))
final = []
for i in range(1, num + 1):
	if num % i == 0: 
		final.append(i)
print(final)