import sys

n,m=map(int,input().split())
q=list(map(int,input().split()))
p=list(map(float,input().split()))
if sum(q)>=m:
    print(0.00)
    sys.exit(0)
dp=[[float(m+1)]*(2**n) for i in range(m+1)]
dp[0][0]=0.0
for i in range(1,m+1):
    for cur in range(2**n):
        for j in range(n):
            if cur&(1<<j) and i>=q[j]:
                dp[i][cur]=min(dp[i][cur],dp[i-q[j]][cur^(1<<j)])
        dp[i][cur]=min(dp[i][cur],dp[i-1][cur]+p[i-1])
print(f"{min(dp[m]):.2f}")

'''
3 10
1 3 4
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
'''