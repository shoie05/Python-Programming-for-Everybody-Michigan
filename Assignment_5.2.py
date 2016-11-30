largest = None
smallest = None

while True:
	num = raw_input("Enter a number: ")
	if num == "done" : break
	
	try:
		intNum = int(num) 
	except:
		print "Invalid input"
		continue
    
	if largest is None:
		largest = intNum
	elif intNum > largest:
		largest = intNum
		
	if smallest is None:
		smallest = intNum
	elif intNum < smallest:
		smallest = intNum

print "Maximum is", largest
print "Minimum is", smallest