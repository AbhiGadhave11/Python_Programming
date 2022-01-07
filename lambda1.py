
#Named Function
def Add(a,b):
	return a + b;

# Lambda Function
Addx = lambda a,b : a + b


def main():
	ret = Add(10,20);
	print("Addition is : ",ret);

	ret = Addx(10,20);
	print("Addition is : ",ret);

	print(type(Addx));
	print(type(Add));
	print(lambda a,b : a + b)



if __name__ == "__main__":
	main();