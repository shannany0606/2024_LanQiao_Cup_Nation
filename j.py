import sys
sys.setrecursionlimit(10**8)

n,mod=map(int,input().split())
a=list(map(int,input().split()))
mul=pow(2,n-1,mod)
tot=1
for i in range(2,n+1):
    tot*=i*(i-1)//2
    tot%=mod
mul=mul*tot%mod

if n==1:
    print(a[0]*mul%mod)
    sys.exit(0)

def dfs(n,a):
    if n==2:
        return mul*pow(2,mod-2,mod)%mod*((a[0]+a[1])+a[0]*a[1]%mod)%mod
    tmp=a[:]
    tot=0
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            tmp=tmp[:i]+tmp[i+1:j]+tmp[j+1:]+[tmp[i]+tmp[j]]            
            tot+=dfs(n-1,tmp)
            tmp=a[:]
            tmp=tmp[:i]+tmp[i+1:j]+tmp[j+1:]+[tmp[i]*tmp[j]]
            tot+=dfs(n-1,tmp)
            tmp=a[:]
            tot%=mod
            cnt+=2
    return tot*pow(cnt,mod-2,mod)%mod

print(dfs(n,a))

    