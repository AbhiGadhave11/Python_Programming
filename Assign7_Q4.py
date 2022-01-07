"""
4. Write a program which accept temperature in 
   Fahrenheit and convert it into celsius. 
  (1 celsius = (Fahrenheit -32) * (5/9))
Input : 10
Output : -12.2222 (10 - 32) * (5/9)
Input : 34
Output : 1.11111 (34 - 32) * (5/9)
"""

def Conversion(value) :

	iAns = (int(value)-32) * (5/9);
	return iAns;

def main() :
	print("Welcome to python Programming\n");

	print("Enter Temperature in Fahrenheit");
	no1 = input();

	iret = Conversion(no1);

	print("Temperature in celcius is : ",iret);

if __name__ == "__main__" :
	main();