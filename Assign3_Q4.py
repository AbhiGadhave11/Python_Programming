'''4. Accept one character from user and convert case 
of that character.
Input : a Output : A
Input : D Output : d
'''


def Display(ch):
    #ch1 = a
	if(ch>='A'):
		if(ch<='Z'):
			ch1 = ch.lower();

	if(ch>='a'):
		if(ch<='z'):
			ch1 = ch.upper();

	return ch1;



def main():
	print("Enter the Character");
	no = input();
	ret = Display(no);
	print(ret);

if __name__ == "__main__":
	main();