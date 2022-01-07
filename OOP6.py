
class Demo:

    A = 10;   #class Variable
    def __init__(self):
        print("Inside Costructor");
        self.B = 20   #instance variable


    def fun_instance(self):  #instance method
        print("Inside Instance Method");
        print(self.B)
        print(self.A)
        print(Demo.A) # this is the correct way to access class variable

    @classmethod
    def fun_class(cls):    #class Method
        print("Inside Class Method");
        print(cls.A);
        print(Demo.A)
        #print(cls.B)

    @staticmethod
    def fun_static():
        print("Inside Static Method")
        print(Demo.A)
        #print(Demo.B)

    def __del__(self):
        print("Inside Destructor");

def  main():
    Demo.fun_static()
    

    
  


    

if __name__ == "__main__":
    main();


# Instance method
   # No decorator
  #  self as a parameter
