#1.Program to divide two numbers

def Division(value1,value2):
	Ans = 0;
	Ans = value1 / value2;
	return Ans;

def main():
	print("Enter First Number");
	no1 = int(input());
	print("Enter Second Number");
	no2 = int(input());

	ret = Division(no1,no2);
	print("Division is : ",ret);

if __name__ == "__main__":
	main();