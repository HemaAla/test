n=int(input("enter n\n"))
arr=list(map(int,input("enter values\n").split()))
#print(arr)
small_count=[]
import math
summ=0
for i in range(len(arr)):
	for j in range(len(arr)):
		summ=summ+math.floor(arr[i]/arr[j])
print(summ)


