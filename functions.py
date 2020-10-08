import numpy as np 
import sys

#define a function that returns  a value
def expo(x):
	return np.exp(x)  #return the np e^x function

#define a subroutine that does not return value
def show_expo(n):
	for i in range(n):
		print(expo(float(i))) #call the expo function

#define a main function
def main():
	n = 10 #provide a default value

	#check if there's a command line argument provided
	if(len(sys.argv)>1):
		n = int(sys.argv[1])

	print("The value of n is ",n)

	show_expo(n)


#run the main function
if __name__ == "__main__":
	main()