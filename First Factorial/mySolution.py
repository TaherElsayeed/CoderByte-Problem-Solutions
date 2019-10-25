#	Problem URL:	https://coderbyte.com/editor/First%20Factorial:Python3
#	Question:
#	Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 
#	4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input 
#	will always be an integer. 

def FirstFactorial(num):

	# code goes here
	data = []
	for x in range(num):	#	Creates a list of every number from 1 to the arguement
		if x == 0:
			pass
		else:
			data.append(x)
	data.append(num)

	product = 1
	for x in data:	# 	Multiples every number in the list together
		product *= x
	return product	# 	Returns the factorial of the arguement

# keep this function call here 
print(FirstFactorial(input()))
