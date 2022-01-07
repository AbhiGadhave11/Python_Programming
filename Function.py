
def Arithmetic(value1,value2) :
	add = value1 + value2;
	sub = value1 - value2;
	return add,sub

def main() :
	print("Enter First number");
	no1 = int(input())

	print("Enter Second number");
	no2 = int(input());

	ret1,ret2 = Arithmetic(no1,no2);
	print("Addition is : ",ret1);
	print("Subtraction is : ",ret2);


if __name__ == "__main__" :
	main();