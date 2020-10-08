
#string

s = "I am a string."
print("The type of s is ",type(s)) #str

#Boolean
yes = True
print("The type of yes is ",type(yes)) #bool true

no = False
print("The type of no is ",type(no)) #bool false


# List -- ordered and changeable
alpha_list = ["a","b","c"] #initialize list

print("The type of alpha_list is ",type(alpha_list)) #list
print("The type of alpha_list[0] is ",type(alpha_list[0]))
alpha_list.append("d") #add d to the end of the list
print(alpha_list)

#Tuple -- ordered and unchangeable list
alpha_tuple = ("a","b","c")
print(type(alpha_tuple))

try:
	alpha_tuple[2] = "d"	#it won't work; results in a TypeError
except TypeError:
	print("We can't add elements to tuples!")
print(alpha_tuple)