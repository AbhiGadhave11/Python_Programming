'''
1.Write a program which accept one number from user 
and print that number of even numbers on screen.
Input : 7
Output: 2 4 6 8 10 12 14
'''

def Display(value):
	no = 2;
	i = 0;
	while(1):
		if(i == value):
			break;
		print(no);
		no = no + 2;
		i = i+1;

def main():
	print("Enter Number");
	no = int(input());
	Display(no);

if __name__ == "__main__":
	main();