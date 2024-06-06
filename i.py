n,y=map(int,input().split())
ans=0
mod=10**9+7
for i in range(max(1,y),n+1,2024):
    for j in range(1,i):
        if '2' not in str(j) and '4' not in str(j):
            for k in range(j+1,i):
                if '2' not in str(k) and '4' not in str(k):
                    t=i-j-k
                    if t<=k:break
                    if '2' not in str(t) and '4' not in str(t):
                        ans+=1
                        #print(j,k,i-j-k)
print(ans%mod)
