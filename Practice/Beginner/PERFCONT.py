tc = int(input())
for _ in range(tc):
    N,P = map(int,input().split())
    L = list(map(int,input().split()))[:N]
    cake,hard = 0,0
    easy,goat = P//2,P//10
    for i in L:
        if(i>=easy):
            cake+=1
        elif(i<=goat):
            hard+=1
    if(cake==1 and hard==2):
        print("yes")
    else:
        print("no")