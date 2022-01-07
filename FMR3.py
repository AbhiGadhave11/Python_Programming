from functools import reduce

data = [5,7,6,8,4];
print("Original Data is : ",data)

print("Data after reduce is : ",reduce(lambda a,b: a + b,list(map(lambda no : no + 2,list(filter(lambda no : (no%2==0),data))))));
