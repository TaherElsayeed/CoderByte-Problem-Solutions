def AlphabetSoup(str):

  # code goes here
  data = []
  for x in range(len(str)):
    data.append(str[x])
    
  data = sorted(data)
  return ''.join(data)

# keep this function call here 
print(AlphabetSoup(input()))
