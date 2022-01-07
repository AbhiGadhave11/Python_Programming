'''1.Write a program which accept number from user 
and return the count of even digits.
Input : 2395
Output : 1
Input : 1018
Output : 2
Input : -1018
Output : 2
Input : 8462
Output : 4
'''

def Zerox(no):
	iDigit = 0;
	iCnt = 0;
	if(no < 0):
		no = -no;
	while(no>0):
		iDigit = no % 10;
		if(iDigit %2 == 0):
			iCnt = iCnt + 1;
		no = int(no / 10);
    
	return iCnt;
	

def main():
	no = 0;
	print("Enter Number");
	no =  int(input());
	bRet = Zerox(no);
	print("Frequency of Digits which are Even : ",bRet);


if __name__ == "__main__":
	main();