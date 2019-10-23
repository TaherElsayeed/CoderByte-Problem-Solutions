def LetterChanges(str):

  # code goes here
  vowles = ["a", "e", "i", "o", "u"]

  alphabet = "abcdefghijklmnopqrstuvwxyz"
  alphabetArray = []
  for x in range(len(alphabet)):
  	alphabetArray.append(alphabet[x])

  data = []

  for x in range(len(str)): 
  	data.append(str[x])

  newData = []
  for x in data:
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


  for x in range(len(newData)):
  	for y in vowles:
  		if newData[x] == y:
  			newData[x] = newData[x].upper()

  foo = ''.join(newData)
  return foo

# keep this function call here 
print(LetterChanges(input()))
