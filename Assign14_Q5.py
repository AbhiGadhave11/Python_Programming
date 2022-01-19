'''5. Accept number of rows and number of columns 
from user and display below pattern.

Input : iRow = 4 iCol = 4
Output : 
1 2 3 4
2 3 4
3 4
4
'''
def Pattern(iRow,iCol):

	for i in range(iRow,0,-1):
		for j in range(1,i+1,1):

			print(j,end=" ")

		print()

def main():
	print("Enter Number of Rows")
	no1 = int(input())
	print("Enter Number of Columns")
	no2 = int(input())

	Pattern(no1,no2)

if __name__ =="__main__":
	main()