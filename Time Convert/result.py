#	Problem URL:	https://coderbyte.com/editor/Time%20Convert:JavaScript
#	Question:	Have the function TimeConvert(num) take the num parameter being passed and return the number of hours and minutes 
#	the parameter converts to (ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a 
#	colon. 

def TimeConvert(num):

	# code goes here
	hours = 0
	minutes = 0
	hours = num // 60	#	Floor division
	minutes = num % 60	#	Mod operation
	return str(hours) + ":" + str(minutes)

# keep this function call here 
print(TimeConvert(input()))
