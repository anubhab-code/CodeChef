tc=int(input())

for i in range(tc):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    r=sorted(arr)
    largest_divisor=0
    for i in r:
        if k % i == 0:
            ld = i
    if ld in arr:
        print(ld)
    else:
        print(-1)