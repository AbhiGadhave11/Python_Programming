import array as ARR;

def main():
	print("Demonstration of array in python");


	data = ARR.array('i',[10,20,30,40]);

	print(data);

	print("Length of array is : ",len(data));

	print("Type is : ",type(data));
	#print(data[0]);
	#print(data[1]);

	for i in range(len(data)):
		print(data[i]);
	i = 0;
	while(i<4):
		print(data[i]);
		i = i+1;

	for no in data:
		print(no,end="\t");




if __name__ =="__main__":
	main();


