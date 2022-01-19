'''1. Accept number of rows and number of columns 
from user and display below
pattern.
Input : iRow = 4 iCol = 4
Output : 
A B C D
A B C D
A B C D
A B C D
'''

def Pattern(iRow,iCol):
	no = 0;

	for i in range(65,iRow):
		for j in range(65,iCol):
			print(chr(j),end=" ");
			#no = no + 1;
		print();


def main():
	print("Enter Number of Rows");
	no1 = int(input());
	print("Enter Number of Columns");
	no2 = int(input());
	Pattern(no1,no2);


if __name__ == "__main__":
	main();