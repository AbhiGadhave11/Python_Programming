


def Addition(no1 ,no2):
	ans = no1 + no2;
	return ans;


def main():
	print("ENter First Number");
	no1 = int(input());

	print("Enter Second Number");
	no2 = int(input());

	ans = Addition(no1,no2);
	print("Addition is : ",ans)


if __name__ == "__main__":
	main();