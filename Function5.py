

def Addition(*value):
	sum = 0;
	for i in range(len(value)):
		sum = sum + value[i];

	return sum;

def main():
	ret = Addition(10,20,30,40,50);
	print("Addition is : ",ret);

	ret = Addition(10,20,30,40);
	print("Addition is : ",ret);

	ret = Addition();
	print("Addition is : ",ret);




if __name__ == "__main__":
	main();