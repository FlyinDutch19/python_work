mystring = "Hello"
mylist = []
for letter in mystring:
	mylist.append(letter)
print(mylist)

mylist = [x for x in "word"]
print(mylist)

mylist = [num**2 for num in range(0,10)]
print(mylist)

mylist = [x for x in range(0,11) if x%2==0]
print(mylist)