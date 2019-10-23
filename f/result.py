def FirstFactorial(num):

	# code goes here
	data = []
	for x in range(num):
		if x == 0:
			pass
		else:
			data.append(x)
	data.append(num)

	product = 1
	for x in data:
		product *= x
	return product

# keep this function call here 
print(FirstFactorial(input()))
