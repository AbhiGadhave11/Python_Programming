
def Addition(value1,value2) :
	ans = value1 + value2;
	return ans;

def main():
	print("Marvellous Addition Application")

	no1 = int(input("Enter First Number:"));
	no2 = int(input("Enter Second Number:"));

	iRet = Addition(no1,no2)
	print("Addition is : ",iRet);	

if __name__=="__main__":
	main();	