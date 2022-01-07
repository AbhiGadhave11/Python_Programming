"""
3. Write a program which accept distance in 
   kilometre and convert it into meter. 
  (1 kilometre = 1000 Meter)
Input : 5
Output : 5000
Input : 12
Output : 12000
"""

def Conversion( value) :
	
	iAns = int(value) * 1000;
	return iAns;

def main() :
	print("Welcome to Python Programming");

	print("Enter the Distance in Kilometer");
	no1 = input();

	Ret = Conversion(no1);

	print("Distance in meter is : ",Ret);

if __name__ == "__main__" :
	main();