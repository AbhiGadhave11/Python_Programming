'''
5.Write a program which accept number from user 
and return difference between summation of all 
its factors and non factors.

Input : 12
Output : -34 (16 - 50)
Input : 10
Output : -29 (8 - 37)
'''

def Factors(value):
	iSum = 0;
	iSum1 = 0;
	for i in range(1,value,1):
		if(value % i != 0):
			iSum = iSum + i;

	for i in range(1,value,1):
		if(value % i == 0):
			iSum1 = iSum1 + i;

	return iSum1-iSum;
	

	

def main():
	print("Enter Number");
	no = int(input());
	ret = Factors(no);
	
	print("Difference of Factors and non-factors are : ",ret);
	

if __name__ == "__main__":
	main();