'''
1.Write a program which accept number from user and 
display its multiplication of factors.
Input : 12
Output : 144 (1 * 2 * 3 * 4 * 6)
Input : 13
Output : 1 (1)
Input : 10
Output : 10 (1 * 2 * 5)
'''


def Factors(value):
	iFact = 1;
	for i in range(1,value):
		if(value%i == 0):
			iFact = iFact * i;

	return iFact;

def main():
	print("Enter Number");
	no = int(input());
	ret = Factors(no);
	print("Multiplication of factors is : ",ret);

if __name__ == "__main__":
	main();