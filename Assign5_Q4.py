'''4.Write a program which accept number from user 
and count frequency of 4 in it.
Input : 2395
Output : 0
Input : 1018
Output : 0
Input : 9440
Output : 2
Input : 922432
Output : 1
'''


def Zerox(no):
	iDigit = 0;
	iCnt = 0;

	while(no>0):
		iDigit = no % 10;
		if(iDigit == 4):
			iCnt = iCnt + 1;
		no = int(no / 10);
    
	return iCnt;
	

def main():
	no = 0;
	print("Enter Number");
	no =  int(input());
	bRet = Zerox(no);
	print("Frequency of four is : ",bRet);


if __name__ == "__main__":
	main();