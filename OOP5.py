
class Demo:

    A = 10;   #class Variable
    def __init__(self):
        print("Inside Costructor");
        self.B = 20   #instance variable


    def fun_instance(self):  #instance method
        print("Inside Instance Method");


    @classmethod
    def fun_class(cls):    #class Method
        print("Inside Class Method");

    @staticmethod
    def fun_static():
        print("Inside Static Method")

    def __del__(self):
        print("Inside Destructor");

def  main():
    Demo.fun_class();
    Demo.fun_static();


    obj = Demo();    # object Creation
    obj.fun_instance();

    #obj.fun_static();
    #obj.fun_class();
   

if __name__ == "__main__":
    main();


# Instance method
   # No decorator
  #  self as a parameter
