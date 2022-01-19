'''3. Accept number of rows and number of columns 
from user and display below pattern.
Input : iRow = 3 iCol = 5
Output : 
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
'''

def Pattern(iRow,iCol):

	for i in range(1,iRow+1,1):
		for j in range(iCol,0,-1):
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