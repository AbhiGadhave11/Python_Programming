

class Demo:

    __X = 50;
    def __init__(self):
        self.A = 10;
        self.__B = 20;  # private variable of a class  (Abstraction)

    def fun(self):
        print("Inside fun");
        print(self.A);
        print(self.__B)
        



def main():
    obj = Demo();
    print(obj.A);
    print(Demo.__X)
    #print(obj.__B);
    obj.fun()

if __name__ == "__main__":
    main();


# A is a public Variable
# B is a private variable