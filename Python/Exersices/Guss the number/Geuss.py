import random

max_guess = 10
# Get a random number
num = random.randint(1,100)

print("Guess the number between 1 and 100\nYou have 10 guess")

for i in range(1, max_guess): 
	answer = int(input("guess: "))

	if answer < num:
		print("too small")

	elif answer > num:
		print("too big")
	else: # the answer is equal the number
		break
	
if answer == num:
	print(f"that's right! the number is *{num}*, you guessed it in {i} guesses")
else:
	print("You guessed 10 times but you failed!")
