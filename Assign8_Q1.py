'''1.Write a program which accept range from user and 
display all numbers in between that range.
Input : 23 35
Output : 23 24 25 26 27 28 29 30 31 32 33 34 35
Input : 10 18
Output : 10 11 12 13 14 15 16 17 18
Input : 10 10
Output : 10
Input : -10 2
Output : -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2
Input : 90 18
Output : Invalid range
'''

def Pattern(no1,no2):

	if(no1>no2):
		print("Invalid Range");
	else:
		for i in range(no1,no2+1,1):
			print(i," ",end="");

		print();

def main():
	no1 = 0;
	no2 = 0;
	print("Enter Starting point");
	no1 = int(input());
	print("Enter Ending point");
	no2 = int(input());
	Pattern(no1,no2);

if __name__ == "__main__":
	main();