from functools import reduce


def main():

	data = [5,7,6,8,4];
	print("Original Data is : ",data)

	#filter(function,list)
	newdata = list(filter(lambda no : (no%2==0),data));

	print("Data after Filter : ",newdata);

	#map(function,list)
	IncrementData = list(map(lambda no : no + 2,newdata))

	print("Data after map : ",IncrementData);

	#reduce(function,list)
	ret = reduce(lambda a,b: a + b,IncrementData);

	print("Data after reduce is : ",ret);


if __name__ == "__main__":
	main();