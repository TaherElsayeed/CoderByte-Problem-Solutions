# This program assumes that the arguement num is a positive integer

def SimpleAdding(num):

  # code goes here
  data = []
  for x in range(num):
    data.append(x)
  data.append(num)
  
  sum = 0
  for x in data:
    sum += x
  return sum

# keep this function call here 
print(SimpleAdding(input()))
