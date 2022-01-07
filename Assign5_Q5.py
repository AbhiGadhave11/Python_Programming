'''5.Write a program which accept number from user 
and count frequency of such a digits which are 
less than 6.
Input : 2395
Output : 3
Input : 1018
Output : 3
Input : 9440
Output : 3
Input : 96672
Output : 1
'''


def Zerox(no):
	iDigit = 0;
	iCnt = 0;

	while(no>0):
		iDigit = no % 10;
		if(iDigit < 6):
			iCnt = iCnt + 1;
		no = int(no / 10);
    
	return iCnt;
	

def main():
	no = 0;
	print("Enter Number");
	no =  int(input());
	bRet = Zerox(no);
	print("Frequency of Digits which are less than 6 are : ",bRet);


if __name__ == "__main__":
	main();