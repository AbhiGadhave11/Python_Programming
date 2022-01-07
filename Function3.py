
# Default Argument
def Area(radius,PI=3.14):
	ans = 0.0;

	ans = PI * radius * radius;

	return ans;


def main():
	print("Enter radius of Circle");
	value  = float(input());


	ret = 0.0;
	ret = Area(radius = value); #Error
	#ret = Area(PI = 7.10,radius = value)
	print("Area of Circle is : ",ret);
	

if __name__ == "__main__":
	main();