sum=0
tc=int(input())
for j in range(tc):
	a=int(input())
	for i in range(a):
		c=input().split(" ")
		price=int(c[0])
		item=int(c[1])
		tax=int(c[2])
		mid_p=price*(tax/100)
		mid_p=price+mid_p
		finalp=mid_p*(tax/100)
		lost =mid_p-finalp
		flost=price-lost
		flost=flost*item
		sum=sum+flost
		i+=1
	print(sum)
	sum=0