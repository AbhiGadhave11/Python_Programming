'''2. Write a program which accept range from user 
and display all even numbers in between that range.

Input : 23 35
Output : 24 26 28 30 32 34
Input : 10 18
Output : 10 12 14 16 18
Input : 10 10
Output : 10
Input : -10 2
Output : -10 -8 -6 -4 -2 0 2
Input : 90 18
Output : Invalid range
'''


def Pattern(no1,no2):

	if(no1>no2):
		print("Invalid Range");
	else:
		for i in range(no1,no2+1,1):
			if(i%2==0):
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