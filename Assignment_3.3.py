str = raw_input("Enter Score between 0.0 and 1.0: ")

try:
	score = float(str)
except:
	print "Entered value is not valid"
	#exit
	quit()

if score >= 0.9:
	print "A"
elif score >= 0.8:
	print "B"
elif score >= 0.7:
	print "C"
elif score >= 0.6:
	print "D"
else:
	print "F"