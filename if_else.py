import random as r
hungry = r.randint(0,2)
if hungry == 2:
	print("I'm hungry!")
elif hungry == 1:
	print("I'm not so hungry, but I want to eat something.")
else:
	print("I'm not hungry.'")