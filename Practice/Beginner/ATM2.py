n=int(input())
li=[]
for i in range(n):
    a,b=map(int,input().split())
    l=[]
    l=[int(i) for i in input().split()]
    c=''
    for i in l:
        if i<=b:
            b=b-i
            c=c+'1'
        else:
            c=c+'0'
    li.append(c)        
for i in li:
    print(i)  