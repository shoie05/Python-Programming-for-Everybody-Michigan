def computepay(iHrs, ratePerHr):
	if(iHrs > 40):
		return (iHrs - 40) * ratePerHr * 1.5 + 40 * ratePerHr
	else:
		return iHrs * ratePerHr
		
hrs = raw_input("Enter Hours: ")
iHrs = float(hrs)

rate = raw_input("Enter Rate: ")
ratePerHr = float(rate)

pay = computepay(iHrs, ratePerHr)

print pay