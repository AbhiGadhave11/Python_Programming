'''3. Accept on number from user if number is less 
than 10 then print “Hello” otherwise print “Demo”.
'''

def Display(value):
	if(value<10):
		print("hello");
	else:
		print("Demo");

def main():
	print("Enter Number");
	no = int(input());
	Display(no);

if __name__ == "__main__":
 	main();