tc=int(input())
for s in range(tc):
	n=int(input())
	l=list(map(int,input().split()))
	l.sort(reverse=True)
	first,second=0,0
	if n==1:
		print("first")
	elif n==2:
		if l[0]==l[1]:
			print("draw")
		else:
			print("first")
	else:
		first+=l[0]
		second+=l[1]
		for i in range(2,len(l)):	
			if i%2!=0:
				first+=l[i]
			else:
				second+=l[i]
		print("draw" if first==second else "first" if first>second else "second")