# Use for, .split(), and if to create a Statement that will print out words that start with "s"
st = "Print only the words that start with S in this sentence"
mylist = []
for word in st.split():
	if word[0].lower() == "s":
		mylist.append(word)
print(mylist)

# Use range() to print all the even numbers from 0 to 10.
mylist = []
for num in range(0,11):
	if num % 2 ==0:
		mylist.append(num)
print(mylist)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
mylist = [num for num in range(1,51) if num%3==0]
print(mylist)

# Go through the string below and if the length of a word is even print "even!"
st = "Print every word in this sentence that has an even number of letters"
mylist = []
for word in st.split():
	if len(word)%2==0:
		mylist.append("even!")
	else:
		mylist.append(word)
print(mylist)

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
mylist = []
for num in range(1,101):
	if num % 3 == 0 and num % 5 != 0:
		mylist.append("Fizz")
	elif num % 5 == 0 and num % 3 != 0:
		mylist.append("Buzz")
	elif num % 3 == 0 and num % 5 == 0:
		mylist.append("FizzBuzz")
	else:
		mylist.append(num)
print(mylist)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = "Create a list of the first letters of every word in this string"
mylist = [word[0] for word in st.split()]
print(mylist)