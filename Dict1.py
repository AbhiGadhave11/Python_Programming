


def main():
	#       Python PPA   LSP   LB
	fees = [12500,15000,21000,15500];

	print(fees);

	print("Please Enter Batch Name");
	batch = input();

	print("Your Entered Batch Name : ",batch);

	if(batch == "PPA"):
		print("Fees are : ",fees[1]);
	elif(batch == "LSP"):
		print("Fees are : ",fees[2]);
	elif(batch == "Python"):
		print("Fees are : ",fees[0]);
	elif(batch == "Angular"):
		print("Fees are : ",fees[3]);
	else :
		print("There is no such batch in Marvellous");




if __name__ == "__main__":
	main();