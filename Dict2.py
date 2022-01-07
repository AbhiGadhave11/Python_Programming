


def main():
	#       Python PPA   LSP   LB
	#fees = [12500,15000,21000,15500];

	fees = {"Python":12500,"PPA":15000,"LSP":21000,"Angular":15000}
    
	print(fees);

	print("Please Enter Batch Name");
	batch = input();

	print("Your Entered Batch Name : ",batch);

	print("Fees are : ",fees[batch]);





if __name__ == "__main__":
	main();