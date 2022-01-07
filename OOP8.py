
class Demo:

    __X = 50;
    def __init__(self):
        self.A = 10;
        self.__B = 20;  # private variable of a class  (Abstraction)

    def fun(self):
        print("Inside fun");
        self.__gun();
        
    def __gun(self):         #private method of a class
        print("Inside gun");
        



def main():
    obj = Demo();
   
    obj.fun()
    #obj.__gun()

if __name__ == "__main__":
    main();


# A is a public Variable
# B is a private variable
#fun is a public
# gun is a private