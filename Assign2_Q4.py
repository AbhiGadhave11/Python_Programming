'''4. Accept one number and check whether is is 
  divisible by 5 or not.
 '''

def Display(value):
	if(value%5 == 0):
		return True;
	else:
		return False;


def main():
	print("Enter Number");
	no = int(input());

	ret = Display(no);
	if(ret == True):
		print("Number is Divisible by 5");
	else:
		print("Number is not Divisible by 5");

if __name__ == "__main__":
 	main();