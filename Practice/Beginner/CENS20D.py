tc= int(input())
while tc>0:
    n=int(input())
    a=[int(i) for i in input().split()]
    c=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]&a[j]==a[i]:
                c+=1
    print(c)
    tc=tc-1