# Encapsulation-> Class = Characteristics + Behaviour

#class Defination
class Arithmetic:
	
	def __init__(self,a,b):  # Constructor
		print("Inside init (constructor)")
		self.no1 = a   # Characteristics
		self.no2 = b   # Characteristics

	def Addition(self):   # Behaviour
		ans = self.no1 + self.no2;
		return ans;
		#print("Inside Addition");


def main():

	print("Enter First Number");
	x = int(input())

	print("Enter second Number");
	y = int(input());

	obj = Arithmetic(x,y);
	ret = obj.Addition();

	print("Addition is : ",ret);


if __name__=="__main__":
	main();