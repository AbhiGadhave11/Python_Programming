"""1.Write a program which accept radius of circle 
  from user and calculate its area.
  Consider value of PI as 3.14.
  (Area = PI * Radius * Radius)
"""

def Area(radius) :

	PI = 3.14;

	Ans = float(PI) * float(radius) * float(radius);
	return Ans;

def main() :
	print("Welcome to python programming");

	print("Enter the radius of circle");

	radius = input();

	iRet = Area(radius);

	print("Area of Circle is : ",iRet);

if __name__ == "__main__" :
	main();