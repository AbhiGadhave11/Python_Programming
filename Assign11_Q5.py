'''5. Accept number of rows and number of columns 
from user and display below pattern.

Input : iRow = 3 iCol = 4
Output : 
1 2 3 4
5 6 7 8
9 10 11 12
'''

def Pattern(iRow,iCol):
	no = 1;

	for i in range(iRow):
		for j in range(iCol):
			print(no,end=" ");
			no = no + 1;
		print();


def main():
	print("Enter Number of Rows");
	no1 = int(input());
	print("Enter Number of Columns");
	no2 = int(input());
	Pattern(no1,no2);


if __name__ == "__main__":
	main();