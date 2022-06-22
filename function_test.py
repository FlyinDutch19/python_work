'''# Lesser of two evens: Write a function that returns the lesser of two given numbers if both nubmers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
	if a % 2 == 0 and b % 2 == 0:
		print(min(a,b))
	else:
		print(max(a,b))

lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)

# Animal crackers: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
	mylist = text.split()
	if mylist[0][0] == mylist[1][0]:
		print(True)
	else:
		print(False)

animal_crackers('Leverlheaded Llama')
animal_crackers('Crazy Kangaroo')

# Old MacDonald: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
	new_name = ''
	name_1 = name[0:3]
	name_2 = name[3:]
	new_name = name_1.capitalize() + name_2.capitalize()
	print(new_name)

old_macdonald('macdonald')

# Master Yoda: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
	text_list = text.split()
	reverse_text_list = text_list[::-1]
	reverse_text = ""
	for word in reverse_text_list:
		reverse_text = reverse_text + word + " "
	print(reverse_text.rstrip())

master_yoda('I am home')
master_yoda('We are ready')

# Almost There: Given an integer n, return True if n in within +-10 of either 100 or 200
def almost_there(n):
	if (90 <= n and n <= 110) or (190 <= n and n <= 210):
		print(True)
	else:
		print(False)

almost_there(104)
almost_there(150)
almost_there(210)


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
def has_33(nums):
	for i in range(0,len(nums)-1):
		if nums[i] == 3 and nums[i+1] == 3:
			return(True)
	return(False)		

result = has_33([1,3,1,3])
print(result)

#Paper Doll: Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
	text_list = ""
	for i in range(0,len(text)):
		text_list = text_list + text[i] * 3
	print(text_list)

paper_doll('Hello')

# BlackJack: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, rturn 'BUST'
def blackjack(a,b,c):
	bj_sum = sum([a,b,c])
	if bj_sum <= 21:
		print(bj_sum)
	elif bj_sum <= 31 and 11 in [a,b,c]:
		print(bj_sum - 10)
	else:
		print("BUST")

blackjack(5,6,7)
blackjack(9,9,9)
blackjack(9,9,11)

# Summer of '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
	total = 0
	add = True

	for num in arr:
		while add:
			if num != 6:
				total += num
				break
			else:
				add = False
		while not add:
			if num != 9:
				break
			else:
				add = True
				break
	print(total)
	

summer_69([1,3,5])
summer_69([4,5,6,7,8,9])
summer_69([2,1,6,9,11])

# Spy Game: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
	code = [0,0,7,'x']
	for num in nums:
		if num == code[0]:
			code.pop(0)
	if len(code) == 1:
		print(True)
	else:
		print(False)

spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])'''

























