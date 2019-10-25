#	Problem URL: https://coderbyte.com/editor/Alphabet%20Soup:Python3
#	Question:
#	Have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the letters in
#	alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.

def AlphabetSoup(str):

	# code goes here
	data = []
	for x in range(len(str)):	# Turns a string into a list where each index is where a char is located
	data.append(str[x])

	data = sorted(data)	#	Sorts the list in alphabetical order
	return ''.join(data)	#	Combines the list into a stirng

# keep this function call here 
print(AlphabetSoup(input()))
