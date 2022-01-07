'''5.Write a program which accept number from user 
and return difference between summation of 
even digits and summation of odd digits.
Input : 2395
Output : -15 (2 - 17)
Input : 1018
Output : 6 (8 - 2)
Input : 8440
Output : 16 (16 - 0)
Input : 5733
Output : -18 (0 - 18)
'''

def Zerox(no):
	iDigit = 0;
	iSum1 =0;
	iSum2 = 0;
	if(no < 0):
		no = -no;
	while(no>0):
		iDigit = no % 10;
		if(iDigit % 2 == 0):
			iSum1 = iSum1 + iDigit;
		if(iDigit %2!=0):
			iSum2 = iSum2 + iDigit;
		no = int(no / 10);
    
	return iSum1-iSum2;
	

def main():
	no = 0;
	print("Enter Number");
	no =  int(input());
	bRet = Zerox(no);
	print("Multiplication of Digits is : ",bRet);


if __name__ == "__main__":
	main();