'''3.Write a program which accept number from user 
and return the count of digits in between 3 and 7.
Input : 2395
Output : 1
Input : 1018
Output : 0
Input : 4521
Output : 2
Input : 9922
Output : 0
'''

def Zerox(no):
	iDigit = 0;
	iCnt = 0;
	if(no < 0):
		no = -no;
	while(no>0):
		iDigit = no % 10;
		if(iDigit>3 and iDigit<7):
			iCnt = iCnt + 1;
		no = int(no / 10);
    
	return iCnt;
	

def main():
	no = 0;
	print("Enter Number");
	no =  int(input());
	bRet = Zerox(no);
	print("Frequency of Digits which are in between 3 and 7 : ",bRet);


if __name__ == "__main__":
	main();