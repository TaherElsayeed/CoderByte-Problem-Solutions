#	The proof for this solution is in Pentagonal Numbers/PROOF.md
# 	The proper solution for this problem should be done with recursion
#	Problem URL:	https://www.coderbyte.com/editor/Pentagonal%20Number:Python3
#	Question:
#	Have the function PentagonalNumber(num) read num which will be a positive integer and determine how many dots exist in a 
#	pentagonal shape around a center dot on the Nth iteration. For example, in the image below you can see that on the first 
#	iteration there is only a single dot, on the second iteration there are 6 dots, on the third there are 16 dots, and on the 
#	fourth there are 31 dots. Your program should return the number of dots that exist in the whole pentagon on the Nth iteration. 

def PentagonalNumber(num):

	#	Code goes here
	numbers = []

	for x in range(num):	# Gets every number from 1 to the arguement and append it to a list
		if x == 0:
			pass
		else:
			numbers.append(x)

	numbers.append(num)	#	Appends the arguement to the end of the list
	sum = 0

	for x in numbers:	#	Performs the proof described in Pentagonal Numbers/PROOF.md
		if x == 1:
			sum += 1
		else:
			sum += (x - 1) * 5

	return sum

#	Keep this function call here 
print(PentagonalNumber(input()))
