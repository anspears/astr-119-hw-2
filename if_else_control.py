#define a function
def flow_control(k):
	print("Value of k = ",k)

	#define a string based on the value of k
	print("Does k equal 0?",(k==0))
	
	if(k==0):
		s = "Variable k = %d equals 0." % k

	elif(k==1):
		s = "Variable k = %d equals 1." % k

	else:
		s = "Variable k = %d does not equal 0 or 1." % k

	#print the variable
	print(s)

#define a main function
def main():

	i=0
	#try flow_control for 0, 1, 2
	flow_control(i)
	i=1
	flow_control(i)
	i=2
	flow_control(i)

if __name__ == "__main__":	#run the program
	main()