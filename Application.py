#import Marvel
#from Marvel import *
import Marvel as M
import Infosystems

def main():
	print("Inside module:",__name__);
	no1 = int(input("Enter first element : "))
	no2 = int(input("Enter Second element : "));
	ret = M.Addition(no1,no2);
	print("Addition is : ",ret);
	ret = Infosystems.Subtraction(no1,no2);
	print("Subtraction is : ",ret);

if __name__ == "__main__" :
	main()