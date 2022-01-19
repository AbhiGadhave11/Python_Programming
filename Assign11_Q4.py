'''4. Accept number of rows and number of columns 
from user and display below pattern.

Input : iRow = 4 iCol = 5
Output : 
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
'''

def Pattern(iRow,iCol):

	for i in range(iRow,0,-1):
		for j in range(iCol,0,-1):
			print(i,end=" ");
		print();

def main():
	no1 = 0;
	no2 = 0;
	print("Enter Number of Rows");
	no1 = int(input());

	print("Enter Number of Columns");
	no2 = int(input());
	Pattern(no1,no2);

if __name__=="__main__":
	main();