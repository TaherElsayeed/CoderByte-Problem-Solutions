#	Problem URL:	https://coderbyte.com/editor/First%20Reverse:Python3
#	Question:
#	Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: 
#	if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH. 

def FirstReverse(str):

# code goes here 
foo = len(str)
bar = []
	for x in range(foo):	#	Iterates over the length of the input and appends the letters in reverse order
		if x == 0:	# 	Skips over the first instance because 0 is not a negative numbeer
			pass
		else:
			bar.append(str[-x])
	bar.append(str[0])	#	Appends the first letter of the str to the end of the array
	return ''.join(bar)	# 	Returns a new string that is the combination of all of the chars in the list

# keep this function call here
print(FirstReverse(input()))	# 	Prints the output of the function and takes a user input as well
