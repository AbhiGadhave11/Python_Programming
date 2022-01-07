'''4.Write a program which accept number from user 
and return multiplication of all digits.
Input : 2395
Output : 270
Input : 1018
Output : 8
Input : 9440
Output : 144
Input : 922432
Output : 864
'''

def Zerox(no):
	iDigit = 0;
	iMulti = 1;
	if(no < 0):
		no = -no;
	while(no>0):
		iDigit = no % 10;
		if(iDigit == 0):
			no = int(no / 10);
			continue;
		iMulti = iMulti * iDigit;
		no = int(no / 10);
    
	return iMulti;
	

def main():
	no = 0;
	print("Enter Number");
	no =  int(input());
	bRet = Zerox(no);
	print("Multiplication of Digits is : ",bRet);


if __name__ == "__main__":
	main();