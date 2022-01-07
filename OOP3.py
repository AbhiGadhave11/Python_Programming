
class Demo:
	A = 10;

	def __init__(self):
		self.B = 30;


	def fun(self):
		print("Inside instance method fun")

	@classmethod
	def gun(cls):
		print("Inside class method");



def main():
	

	obj1 = Demo()

	print("Value of instance Variable : ",obj1.B);

	print("Value of class Variable : ",Demo.A);
	Demo.gun()


if __name__ == "__main__":
	main();