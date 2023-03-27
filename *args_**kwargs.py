# 用*args 和 **kwargs在function中允许输入任意数量的元素，而不用提前定义对应数量：

def myfunc(*args): #args其实可以用任何名称代替，关键是要有*
	print(args) #将输入的元素自动放到一个tuple里
	return sum(args) * 0.05

print(myfunc(4,1,532,41,2134))


def myfunc(**kwargs): #**与上面单独的*区别是，可以创建dictionary
	print(kwargs)
	if "fruit" in kwargs:
		print(f"My choice of fruit is {kwargs['fruit']}")
	else:
		print("I did not find any fruit here.")

myfunc(fruit="apple",veggi="lettuce")

# 还可以把*args和**kwargs同时放在一起用
def myfunc(*args,**kwargs):
	print(args)
	print(kwargs)
	print(f"I would like {args[0]} {kwargs['food']}.")

myfunc(10,20,30,fruit="apple",food="eggs",animal="dog")