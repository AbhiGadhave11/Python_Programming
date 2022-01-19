'''3. Accept number of rows and number of columns from 
user and display below pattern.
Input : iRow = 6 iCol = 6
Output : 
* * * * * *
* *       *
*   *     *
*     *   *
*       * *
* * * * * *
'''

def Pattern(iRow,iCol):
	for i in range(1,iRow+1):
		for j in range(1,iCol+1):
			if((i==j) or (i==1 and j<=iCol) or (i==iRow and j<=iCol) or(j==1 and i<=iRow) or (j==iCol and i<=iRow)):
				print("*",end=" ");
			else:
				print(" ",end=" ")
		print()

def main():
	print("Enter Number of Rows")
	no1 = int(input())
	print("Enter Number of Columns")
	no2 = int(input())

	Pattern(no1,no2)


if __name__ == "__main__":
	main()