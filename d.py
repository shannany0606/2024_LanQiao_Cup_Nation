ans=0
n,m,l=map(int,input().split())
a=list(map(int,input().split()))
dat={}
for x in a:
    dat[x//n]=dat.get(x//n,0)+1
    if dat[x//n]<=m:ans+=1
print(ans)