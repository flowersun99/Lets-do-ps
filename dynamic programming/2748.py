#피보나치 수 2
def fibonacci(n):
    dp=[0]*(n+1)
    dp[1],dp[2]=1,1
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[-1]

n=int(input())

if n == 1:
    print(1)
    exit()
else:
    print(fibonacci(n))