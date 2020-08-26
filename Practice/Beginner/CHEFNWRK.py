tc=int(input())
for _ in range(tc):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=k
    a,b=0,0
    for i in range(n):
        if l[i]>k:
            b=1
            print(-1)
            break
        else:
            if s-l[i]>=0:
                s=s-l[i]
            else:
                a+=1
                s=k-l[i]
    if b!=1:
        print(a+1)