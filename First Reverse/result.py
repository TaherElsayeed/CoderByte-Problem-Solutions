def FirstReverse(str):

# code goes here 
	foo = len(str)	# Gets the length of the input
	bar = []	# Creates an empty list to store the chars of the str in reverse order
	for x in range(foo):	# Iterates over the length of the input and appends the letters in reverse order
		if x == 0:	# Skips over the first instance because 0 is not a negative numbeer
			pass
		else:
			bar.append(str[-x])
	bar.append(str[0])	# Appends the first letter of the str to the end of the array
	faz = ''.join(bar)	#	Creates one string from the array of chars
	return faz	# Returns the new string

# keep this function call here
print(FirstReverse(input()))	# Prints the output of the function and takes a user input as well
