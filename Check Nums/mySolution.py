#	Problem URL:	https://coderbyte.com/editor/Check%20Nums:Python3
#	Question:
# 	Have the function CheckNums(num1,num2) take both parameters being passed and return the string true if num2 is greater than
#	num1, otherwise return the string false. If the parameter values are equal to each other then return the string -1.

def CheckNums(num1,num2):

	#	Code goes here
	if num1 < num2:
		return True
	
	if num1 > num2:
		return False
	
	return -1

#	Keep this function call here 
print(CheckNums(input(),input()))
