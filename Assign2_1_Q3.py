'''4. Accept two numbers from user and display first 
number in second number of times.
'''


def Display(value1,value2):
	
	for i in range(value2):
		print(value1);

def main():
	print("Enter first Number");
	no1 = int(input());
	print("Enter Second Number");
	no2 = int(input());
	Display(no1,no2);

if __name__ == "__main__":
 	main();