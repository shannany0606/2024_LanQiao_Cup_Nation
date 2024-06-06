n=int(input())
a=list(map(int,input().split()))
R=n
cnt={}
while R:
    if a[R-1] in cnt.keys():
        break
    R-=1
    cnt[a[R]]=cnt.get(a[R],0)+1
ans=n-R
#print(0,R,n-R)
for L in range(0,n):
    if a[L] in cnt.keys() and R<n:
        while cnt[a[L]]:
            cnt[a[R]]-=1
            R+=1
    if cnt.get(a[L],0):break
    cnt[a[L]]=cnt.get(a[L],0)+1
    ans=max(ans,L+1+n-R)
    #print(L+1,R,L+1+n-R)
print(ans)
    