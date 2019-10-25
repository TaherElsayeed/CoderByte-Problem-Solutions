def SimpleSymbols(str):

  # code goes here
  response = "false"
  for x in range(len(str)):

    if str[-1].isalpha():
      return response 
    else:
      if x == 0:
        if str[x].isalpha():
          return response
      if str[x].isalpha():
        if str[x - 1] != "+":
          return response
        if str[x + 1] != "+":
          return response
  return "true"
  
# keep this function call here 
print(SimpleSymbols(input()))
