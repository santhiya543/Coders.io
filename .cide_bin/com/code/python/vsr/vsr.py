def calculateFactorial(n):
	total=1
	while(n>1):
		total*=n
		n-=1
	return total