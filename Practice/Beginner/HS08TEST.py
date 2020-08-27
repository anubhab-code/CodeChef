x,y=input().split()
x=float(x)
y=float(y)
if((0<x<=2000)or (0<=y<=2000)):
    if((x%5==0)and((x+0.50)<=y)):
        y=y-x-0.50
        print(y)
    else:
        print(y)