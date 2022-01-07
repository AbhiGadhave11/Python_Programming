'''
4.Write a program which accept number from user 
and return summation of all its non factors.
Input : 12
Output : 50
Input : 10
Output : 37
'''


def Factors(value):
	iSum = 0;
	for i in range(1,value,1):
		if(value % i != 0):
			iSum = iSum + i;

	return iSum;

	

def main():
	print("Enter Number");
	no = int(input());
	ret = Factors(no);
	print("Summation of non-factors are : ",ret);
	

if __name__ == "__main__":
	main();