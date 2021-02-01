name = input("Type your name: ")
age = int(input("Type your age: "))

# Calculate the year the user will be 100 yo
year = (2021 - age + 100)

print(f"Hello {name}, you are {age} years old, you'll be 100 years old in {year}")

# Extra Exersice
many = int(input("Enter an additional number: "))
for i in range(many):
	print(f"Hello {name}, you are {age} years old, you'll be 100 years old in {year}")