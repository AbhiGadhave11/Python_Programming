'''data = (10,20,30,40)

print("Original data : ",data)

data = list(data)

data.append(50)

data = tuple(data)

print("Updated data : ",data)
'''

data = (10,20,30,40);

print("Tuple is : ",data);

lst = list(data);

lst.append(50);

data = tuple(lst);

print("Updated tuple is : ",data);