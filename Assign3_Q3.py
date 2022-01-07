'''3. Write a program which accept number from user 
and print even factors of that number.
Input : 36
Output: 2 6 12 18
'''

def Display(value):
	if(value<0):
		value = -value;

	for i in range(1,value):
		if(value%i == 0):
			if(i%2 == 0):
				print(i);

def main():
	print("Enter Number:");
	no = int(input());
	Display(no);

if __name__ == "__main__":
	main();