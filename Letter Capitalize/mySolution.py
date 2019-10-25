#	Problem URL:	https://coderbyte.com/editor/Letter%20Capitalize:Python3
#	Question:
#	Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words 
#	will be separated by only one space. 

def LetterCapitalize(str):

	# code goes here
	data = str.split()
	for x in range(len(data)):
		data[x] = data[x].capitalize()
	return ' '.join(data)

# keep this function call here 
print(LetterCapitalize(input()))
