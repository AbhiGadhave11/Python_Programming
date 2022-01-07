'''5. Accept on character from user and check whether 
that character is vowel (a,e,i,o,u) or not.
Input : E Output : TRUE
Input : d Output : FALSE
'''


def Display(value):
	if(value=='a'or value=='e' or value=='i' or value=='o' or value=='u'):
		return True;
	else:
		return False;

def main():
	print("Enter Character");
	no = input();
	bret = Display(no);
	if(bret == True):
		print("TRUE");
	else :
		print("FALSE");

if __name__ == "__main__" :
	main();