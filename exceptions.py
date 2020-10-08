#exceptions let you deal with unexpected results

try:
	print(a) #since a is not defined, it'll throw an exception
except:
	print("a is not defined!")

#there are specific errors to help with cases
try:
	print(a)
except NameError:
	print("a is still not defined!")
except:
	print("Something else went wrong.")

#this will break our program since a is not defined
print(a)