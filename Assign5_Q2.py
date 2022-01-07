'''2.Write a program which accept number from user 
and check whether it contains 0 in it or not.
Input : 2395
Output : There is no Zero
Input : 1018
Output : It Contains Zero
Input : 9000
Output : It Contains Zero
Input : 10687
Output : It Contains Zero
'''

def Zerox(no):
	iDigit = 0;

	while(no>0):
		iDigit = no % 10;
		if(iDigit == 0):
			break;
		no = int(no / 10);

	if(no == 0):
		return False;
	else :
		return True;

def main():
	no = 0;
	print("Enter Number");
	no =  int(input());
	bRet = Zerox(no);
	if(bRet == False):
		print("It Does not Contains zero");
	else:
		print("It Contains zero");


if __name__ == "__main__":
	main();