import array as ARR;

def main():
	print("Demonstration of array in python");


	data = ARR.array('f',[10.1,20.2,30.3,40.4]);

	print(data);

	print("Length of array is : ",len(data));

	print("Type is : ",type(data));
	#print(data[0]);
	#print(data[1]);

	for i in range(len(data)):
		print(data[i]);
	i = 0;


	print("Typecode of array is : ",data.typecode);
	



if __name__ =="__main__":
	main();


