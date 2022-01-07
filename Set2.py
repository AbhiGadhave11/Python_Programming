print("Enter Number of Elements");
size = int(input());
data = set();
for i in range(size):
	print("Enter Element no : ",i+1)
	no = int(input());
	data.append(no);


print("Data from set is : ",data);

print("Enter data to search");
value = int(input());

if(value in data):
	print("Element is there");
else:
	print("There is no such Element")
