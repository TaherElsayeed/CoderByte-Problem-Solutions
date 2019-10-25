#	Problem URL:	https://coderbyte.com/editor/Letter%20Changes:Python3
# 	Question:
#	Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
#	Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then 
#	capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 

def LetterChanges(str):

	# 	code goes here
	vowles = ["a", "e", "i", "o", "u"]	# 	List of vowels

	alphabet = "abcdefghijklmnopqrstuvwxyz"
	alphabetArray = []
	for x in range(len(alphabet)):	# 	Creates a list from the alphabet
		alphabetArray.append(alphabet[x])

	data = []

	for x in range(len(str)):	# 	Converts the arguement into a list of chars
		data.append(str[x])

	newData = []
	
	for x in data:	# 	Change the order of letters to suit the needs of the problem
		if x.isalpha():
			for y in range(len(alphabetArray)):
				if x == alphabetArray[y]:
					try:
						newData.append(alphabetArray[y + 1])
					except IndexError:
						newData.append("a")
					break
	else:
		newData.append(x)


	for x in range(len(newData)):	# 	Capitalize vowels
		for y in vowles:
			if newData[x] == y:
				newData[x] = newData[x].upper()

	return ''.join(newData)	# 	Return a string of the all the chars

# 	keep this function call here 
print(LetterChanges(input()))
