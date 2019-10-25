#	This problem should really be called "Longest Phrase" due to it checking not just letters but also alphanumeric charachters
#	Problem URL:	https://coderbyte.com/editor/Longest%20Word:Python3
#	Question:
#	Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are 
#	two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and 
#	assume sen will not be empty.

def LongestWord(sen):

	# code goes here
	data = sen.split()
	wordData = []
	
	for x in data:	# Retrieves only the alphanumeric values from the arguement
		foo = []
		for y in range(len(x)):
			if x[y].isalnum():
				foo.append(x[y])
		wordData.append(''.join(foo))

	max = 0
	index = None
	
	for x in range(len(wordData)):	# Compare the strings in the list and store the index that holds the longest string
		if max < len(wordData[x]):
			max = len(wordData[x])
		index = x

	return wordData[index]	# Return the longest string

# keep this function call here 
print(LongestWord(input()))
