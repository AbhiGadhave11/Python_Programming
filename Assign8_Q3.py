'''3. Write a program which accept range from user 
and return addition of all numbers in between 
that range. 
(Range should contains positive numbers only)
Input : 23 30
Output : 212
Input : 10 18
Output : 126
Input : -10 2
Output : Invalid range
Input : 90 18
Output : Invalid range
'''

def Pattern(no1,no2):
	iSum = 0;

	if(no1>no2 or no1<0 or no2<0):
		print("Invalid Range");
	else:
		for i in range(no1,no2+1,1):
			
			iSum = iSum + i;

	
	return iSum;	

def main():
	no1 = 0;
	no2 = 0;
	print("Enter Starting point");
	no1 = int(input());
	print("Enter Ending point");
	no2 = int(input());
	iRet = Pattern(no1,no2);
	print("Addition of all Numbers between that Range :",iRet);

if __name__ == "__main__":
	main();