def TimeConvert(num):
  
  # code goes here
  hours = 0
  minutes = 0
  hours = num // 60
  minutes = num % 60
  return str(hours) + ":" + str(minutes)

# keep this function call here 
print(TimeConvert(input()))
