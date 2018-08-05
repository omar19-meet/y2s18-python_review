# Write your solution for 1.4 here!

def is_prime(x):
	a=0
	for i in range(2,x):
			if x%i==0:
				a+=1
	if a==1:
		return(False)
		print("False")			
	else:
		return(True)
		print("True")

is_prime(13)
is_prime(4)	
	
