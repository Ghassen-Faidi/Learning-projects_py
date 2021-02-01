import random
# Random Lists
list_1 = []
list_2 = []
final = []

# Make  two random lists
len_list = random.randint(7, 12) # Number of elemnts of the list
for i in range(len_list):
	num_1 = random.randint(1, 20) #Random number
	list_1.append(num_1) # Add the number to the list

len_list = random.randint(7, 12) # Number of elemnts of the list
for i in range(len_list):
	num_2 = random.randint(1, 20)
	list_2.append(num_2)

# Find the longer list
if len(list_1) > len(list_2):
	lenth = len(list_1)
	longer_list = list_1
	smaller_list = list_2
else:
	lenth = len(list_2)
	longer_list = list_2
	smaller_list = list_1

for i in range(lenth):
	x = longer_list[i]
	if x in smaller_list:
		final.append(x)
		
print(f"List 1 = {list_1}\nList 2 = {list_2}")
print(f"The common items are: {final}")
		