#5. Accept number from user and check whether 
#number is even or odd.

def Display(value):
	if(value%2 == 0):
		return True;
	else:
		return False;

def main():
	print("Enter Number");
	no = int(input());
	
	ret  = Display(no);

	if(ret == True):
		print("Number is Even");
	else:
		print("Number is Odd");

if __name__ == "__main__":
 	main();