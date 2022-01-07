'''1.Write a program which accept number from user 
and display its digits in reverse order.
Input : 2395
Output : 
5 9 3 2
Input : 1018
Output : 8
1 0 1
Input : -1018
Output : 8
1 0 1
Input : 9000
Output : 
0 0 0 9
'''

def Reverse(no):
	iDigit = 0;
	while(no > 0):
		iDigit = no % 10;
		print(iDigit);
		no =int(no / 10);

def main():
	no = 0;
	print("Enter Number:");
	no = int(input());
	Reverse(no);

if __name__ == "__main__":
	main();