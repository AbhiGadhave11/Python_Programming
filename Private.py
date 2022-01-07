
class Base:
	def __init__(self):
		self.a = 10;
		self.__c = 20;

class Derived(Base):
	def __init__(self):

		Base.__init__(self)
		print(self.__c)

def main():
	obj = Derived()
	#obj.Display()


if __name__ == "__main__":
	main()