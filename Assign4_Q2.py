'''2.Write a program which accept number from user 
and display its factors in decreasing order.
Input : 12
Output : 6 4 3 2 1
'''


def Factors(value):
	
	for i in range(value-1,0,-1):
		if(value % i == 0):
			print(i);

	

def main():
	print("Enter Number");
	no = int(input());
	Factors(no);
	

if __name__ == "__main__":
	main();