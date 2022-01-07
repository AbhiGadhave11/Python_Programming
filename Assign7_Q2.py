"""
2. Write a program which accept width & height of 
  rectangle from user and calculate its area.
 (Area = Width * Height)
Input : 5.3 9.78
Output : 51.834
"""

def Area(Height,Width) :
	
	iAns = float(Height) * float(Width);
	return iAns;


def main() :
	print("Welcome to Python programming");

	print("Enter the Height");
	no1 = input();

	print("Enter the Width");
	no2 = input();

	iRet = Area(no1,no2);

	print("Area is : ",iRet);

if __name__ == "__main__" :
	main();	