hrs = raw_input("Enter Hours: ")
iHrs = float(hrs)

rate = raw_input("Enter Rate: ")
ratePerHr = float(rate)

if(iHrs > 40):
	pay = (iHrs - 40) * ratePerHr * 1.5 + 40 * ratePerHr
else:
	pay = iHrs * ratePerHr

print pay