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


def main():

	obj1 = Arithmetic(10,11);
	ret = obj1.Addition();
	print("Addition is : ",ret);

	obj2 = Arithmetic(20,21);
	ret = obj2.Addition();
	print("Addition is : ",ret);


if __name__=="__main__":
	main();