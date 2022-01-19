'''2. Accept number of rows and number of columns 
from user and display below pattern.
Input : iRow = 4 iCol = 3
Output : 
1 2 3
1 2 3
1 2 3
1 2 3
'''

def Pattern(iRow,iCol):

	for i in range(1,iRow+1):
		for j in range(1,iCol+1):
			print(j," ",end="");

		print();



def main():
	no1 = 0;
	no2 = 0;
	print("Enter Number of Rows");
	no1 = int(input());
	print("Enter Number of Columns");
	no2 = int(input());

	Pattern(no1,no2);

if __name__ == "__main__":
	main();