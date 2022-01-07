data = {"A":10,"B":20,"C":30,"D":40,51:"D"}

print(data);
print("Type is : ",type(data))
print("Length is : ",len(data))

#print(data[0])  We cannot access with index

#print(data["A"])
#print(data["C"]);


for keys in data:
	print(keys,data[keys]);
