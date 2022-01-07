'''5. Accept one number from user and print that 
  number of * on screen.
 '''

def Display(value):

	for i in range(value):
		print("*");

def main():
	print("Enter Number");
	no = int(input());
	Display(no);

if __name__ == "__main__":
 	main();