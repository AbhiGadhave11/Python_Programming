
class Base:
	def __init__(self):
		print("Inside Base Conctructor")
		self.A = 10;

	def fun(self):
		print("Base fun");


class Derived(Base):
	
	def __init__(self):
		super().__init__();
		#Base.__init__(self)

		print("Inside Derived Conctructor");
		self.B = 20;

	#def gun(self)

	def gun(self) :
		print("Derived gun")




def main():
	dobj = Derived()
	dobj.fun()
	print(dobj.A)
	



if __name__ == "__main__":
	main();