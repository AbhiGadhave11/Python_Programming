
def Maximum(value1,value2) :
	if (value1 > value2) :
		return value1;
	else :
		return value2;


def main() :
	print("Enter First Number");
	no1 = int(input());
	print("Enter Second Number");
	no2 = int(input());

	ret = Maximum(no1,no2);

	print("Maximum Number is : ",ret); 



if __name__ == "__main__":
	main();