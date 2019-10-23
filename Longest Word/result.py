# This problem should really be called "Longest Phrase" due to it checking not just letters but also alphanumeric charachters

def LongestWord(sen):

	# code goes here
	data = sen.split()
	wordData = []
	for x in data:
		foo = []
		for y in range(len(x)):
			if x[y].isalnum():
				foo.append(x[y])
		wordData.append(''.join(foo))

	max = 0
	index = None
	for x in range(len(wordData)):
		if max < len(wordData[x]):
			max = len(wordData[x])
			index = x

	return wordData[index]

# keep this function call here 
print(LongestWord(input()))
