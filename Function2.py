def Addition(no1,no2):
	Ans = 0;
	Ans = no1 + no2;
	return Ans;

def main():
	print("Enter First Number");
	value1 = int(input());

	print("Enter Second Number");
	value2 = int(input());

	#keyword Argument
	ret = Addition(no1=value1,no2=value2);
	print("Addition is : ",ret);



if __name__ == "__main__":
	main();