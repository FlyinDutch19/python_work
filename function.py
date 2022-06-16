'''def add_function(num1,num2):
	return num1+num2

result = add_function(1,2)
print(result)


def say_hello(name="Default"):
	print(f"Hello {name}")

say_hello("Ji")


def check_even_list(num_list):
	#return all the even numbers in a list
	# placeholder variables
	even_numbers = []
	for number in num_list:
		if number % 2 == 0:
			even_numbers.append(number)
		else:
			pass
	return even_numbers

num_list = [1,2,412,5,1341,2,31,24,1,23,1,2,4,1,23]
print(check_even_list(num_list))


# return multiple elements from a function
stock_prices = [("Apple",200), ("Google",400), ("Microsoft",100)]
for ticker,price in stock_prices:
	print(f"The stock prices of {ticker} is US${price}")

def stock_check(stock_prices):
	
	current_max = 0
	most_valuable_stock = ""
	
	for stock,price in stock_prices:
		if price > current_max:
			current_max = price
			most_valuable_stock = stock
		else:
			pass
	
	return (most_valuable_stock,current_max)

stock,price = stock_check(stock_prices)

print(f"The most valuable stock is {stock} with the price of US${price}")'''


# Interactions between Python lists, a small game to guess the position of "O"
from random import shuffle #shuffle的作用是对list中的元素随机打乱重新排序

def shuffle_list(mylist):
	shuffle(mylist)
	return mylist

def player_guess():
	guess = ""
	while guess not in ['0','1','2']:
		guess = input("Pick a nubmer: 0, 1, or 2: ")
	return int(guess)

def check_guess(mylist,guess):
	if mylist[guess] == "O":
		print("Correct!")
	else:
		print("You lose.")
		print(mylist)

if_play = "yes"

while if_play == "yes":
	# Inital list
	mylist = ["","O",""]

	# Shuffle list
	new_list = shuffle_list(mylist)

	# User guess
	guess = player_guess()

	# Check guess
	check_guess(mylist,guess)

	if_play = input("Do you want to play again?(yes/no): ")













