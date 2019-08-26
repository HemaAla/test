import math
t=int(input("enter test cases\n"))
while(t):
	n=int(input("enter n\n"))
	#print( math.ceil(math.log(n, 2)))
	y=0
	x=math.ceil(math.log(n, 2))
	for i in range(1,x+1):
		if(x*i>=n):
			#print(i)
			y=i
			break
	print(x+y)
	t-=1
