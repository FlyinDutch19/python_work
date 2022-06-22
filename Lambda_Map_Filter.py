# map
def square(num):
	return num**2
my_nums = [1,2,3,4,5]
square_list = list(map(square,my_nums))
print(square_list)


# Filter
def check_even(num):
	return num % 2 == 0
my_nums = [1,2,3,4,5,6]
even_numbers = list(filter(check_even,my_nums))
print(even_numbers)

my_nums = [1,2,3,4,5]
print(list(map(lambda num: num**2, my_nums)))

# Lambda
my_nums = [1,2,3,4,5]
a = list(map(lambda num: num**2, my_nums))
print(a)

my_nums = [1,2,3,4,5,6]
a = list(filter(lambda num: num%2==0, my_nums))
print(a)
