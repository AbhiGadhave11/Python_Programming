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

print("Data type is : ",type(Data));
print("Length of list is : ",len(Data))

print("Data From 0th index: ",Data[0]);
print("Data From 3rd index : ",Data[3]);
#print("Data From 3rd index : ",Data[4]);

Data[0]=12;
print(Data);

Data.append(111);
print(Data)

Data.insert(2,51);
print(Data)

