'''
List
Sequential
Indexed
Data is mutable
list is mutable
Allows Duplicate
Heterogeneous Allowed
'''

Data = [11,22,51,101];

print("Data using while loop");

i= 0;
while(i < len(Data)):
	print(Data[i]);
	i = i+1;

print("Data using for loop");

# for i in range(4)
# for i in range(0,1,2,3)

for i in range(len(Data)):
	print(Data[i])