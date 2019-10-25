#	Problem URL:	https://coderbyte.com/editor/Simple%20Symbols:Python3
#	Question:	Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable 
#	sequence by either returning the string true or false. The str parameter will be composed of + and = symbols with several 
#	characters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the 
#	string to the left would be false. The string will not be empty and will have at least one letter. 

def SimpleSymbols(str):

	# code goes here
	response = "false"	#	False code
	
	for x in range(len(str)):	#	Determines if a letter does not have plus signs around it (returns response if so)
		if str[-1].isalpha():
			return response 
		else:
			if x == 0:
				if str[x].isalpha():
					return response
				if str[x].isalpha():
					if str[x - 1] != "+":
						return response
					if str[x + 1] != "+":
						return response
	
	return "true"	#	The desired response code

# keep this function call here 
print(SimpleSymbols(input()))
