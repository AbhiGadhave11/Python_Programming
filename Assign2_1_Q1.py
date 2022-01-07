'''2. Accept one number from user and print that 
number of * on screen.
'''


def Display(value):
	i = 0;
	while(i<value):
		print("*");
		i = i+1;

def main():
	print("Enter Number");
	no = int(input());
	Display(no);

if __name__ == "__main__":
 	main();