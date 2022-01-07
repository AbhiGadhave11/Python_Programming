


import Marvellous as marvel;

def main():
	size = 0;
	print("Enter the Number of elements that you want");
	size = int(input());
	lst = [];
	print("Enter the Elements");
	for i in range(size):
		ele = int(input());

		lst.append(ele);

	#for i in range(len(lst)):
	print(lst);

	iRet = marvel.Addition(lst);
	print("Addition is : ",iRet);


if __name__ == "__main__":
	main();