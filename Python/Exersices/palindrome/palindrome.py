word = list(input("Type a word: ")) #Make a list from the word

if word == word[::-1]:
	print(f"{''.join(word)} is a palindrome" )
else:
	print(f"{''.join(word)} is not a palindrome" )