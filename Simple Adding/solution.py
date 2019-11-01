#	This program assumes that the arguement num is a positive integer
#	Problem URL:	https://coderbyte.com/editor/Simple%20Adding:Python3
#	Question:
#	Have the function SimpleAdding(num) add up all the numbers from 1 to num. For example: if the input is 4 then your program 
#	should return 10 because 1 + 2 + 3 + 4 = 10. For the test cases, the parameter num will be any number from 1 to 1000. 

def SimpleAdding(num):

	# Code goes here
	data = []
	
	for x in range(num):	#	Generates a list of every number from 0 to the arguement including the arguement
		data.append(x)
	
	data.append(num)
	sum = 0
	
	for x in data:	#	Adds all of the values in the list of every number
		sum += x
	
	return sum

# Keep this function call here 
print(SimpleAdding(input()))
