import random
import time

def prog():
	#The random function
	list = ["Rock","Paper","Sissors"]
	pc = random.choice(list)
	#Player input
	hu = input("Rock-------r--\nPaper------p--\nSissors----s-- \nwhat is you choice?: ")
	#result
	def ready():
		print("3!")
		time.sleep(0.7)
		print("2!")
		time.sleep(0.7)
		print("1!")
		print(f"you chose **{hu}**, the PC has chosen **{pc}**")
	win = "||| You win! |||"
	lose = "||| You lose! |||"
	# player choses rock
	if hu == "r":
		hu = list[0] # r becomes rock to make the "draw" condition easier
		#PC conditions
		if pc == "Paper":
			ready()
			print(lose)
		elif pc == "Sissors":
			ready()
			print(win)
	# player choses paper
	elif hu == "p":
		hu = list[1]
		#PC conditions
		if pc == "Rock":
			ready()
			print(win)
		elif pc == "Sissors":
			ready()
			print(lose)
	# playe choses paper
	elif hu == "s":
		hu = list[2]

		#PC conditions
		if pc == "Rock":
			ready()
			print(lose)
		elif pc == "Paper":
			ready()
			print(win)
	#Draw Condition
	if hu == pc:
		ready()
		print("||| it's a draw! |||")

prog()

ans = input("Wanna play again? y/n:")

while ans == "y":
	print("-----------------------------------------")
	prog()
	ans = input("Wanna play again? y/n:")