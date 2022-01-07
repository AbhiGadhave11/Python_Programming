"""
5. Write a program which accept area in square 
   feet and convert it into square meter. 
   (1 square feet = 0.0929 Square meter)
Input : 5
Output : 0.464515
Input : 7
Output : 0.650321
"""

def Conversion(value) :

	iAns = int(value) * 0.0929;
	return iAns;

def main() :
	print("Welcome to Python Programming\n");

	print("Enter the area in square feet");
	no1 = input();

	iRet = Conversion(no1);

	print("Area is : ",iRet);

if __name__ == "__main__" :
	main();	