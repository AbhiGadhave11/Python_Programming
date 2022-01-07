from functools import reduce

#def CheckEven(no):
#	return (no % 2 == 0)

CheckEven = lambda no : (no%2==0)


#def Increment(no):
#	return no + 2;

Increment = lambda no : no + 2;


#def Addition(a,b):
#	return a + b;

Addition = lambda a,b: a + b;


def main():

	data = [5,7,6,8,4];
	print("Original Data is : ",data)

	#filter(function,list)
	newdata = list(filter(CheckEven,data));

	print("Data after Filter : ",newdata);

	#map(function,list)
	IncrementData = list(map(Increment,newdata))

	print("Data after map : ",IncrementData);

	#reduce(function,list)
	ret = reduce(Addition,IncrementData);

	print("Data after reduce is : ",ret);



if __name__ == "__main__":
	main();