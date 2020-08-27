n=int(input())
while(n):
    a=input()
    b=1 
    for i in range(len(a)-1):
        if a[i]!=a[i+1]:
            b=b+1 
    print(b//2)
    n=n-1