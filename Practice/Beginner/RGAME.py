for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    mod = 10**9 + 7
    diff_sum = 0
    temp = A[0]
    x = 1
    for i in range(1,len(A)):
        s1 = temp*A[i]
        diff_sum = 2*diff_sum + s1
        temp += (A[i] * x) 
        x = (x*2) % mod
    print((diff_sum*2)%mod)