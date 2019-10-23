def LetterCapitalize(str):

  # code goes here
  data = str.split()
  for x in range(len(data)):
    data[x] = data[x].capitalize()
  str = ' '.join(data)
  return str

# keep this function call here 
print(LetterCapitalize(input()))
