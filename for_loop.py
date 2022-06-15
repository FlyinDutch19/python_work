my_iterable = [1,2,3,4,5,6,7,8,9,10]
num_even = 0
for num in my_iterable:
	if num % 2 == 0:
		num_even = num_even + 1

if num_even == 0:
	print("There is no even number in the list.")
elif num_even == 1:
	print("There is 1 even number in the list.")
else:
	print(f"There are {num_even} even numbers") #f-string 功能只能在python 3.6以上实现。也可以用 string.format(num_even)的方式实现自动填入的功能

	

d = {"key1":1, "key2":2, "key3":3}
for key in d: #如果不写d.items()，默认是只显示key，而不显示value
	print(key)
for key,value in d.items():
	print(key,value)

