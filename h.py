import sys

n=int(input())
a=list(map(int,input().split()))
if n<=2:
    print(0)
    sys.exit(0)
pre=a[1]-a[0]
ans=0

def check(las,cnt,s,pre):
    s-=las
    tot=0
    while cnt:
        cnt-=1
        tmp=las//2+(las&1)
        tot+=tmp
        las=tmp
    return las<=pre*2 and tot<=s

for i in range(2,n):
    if a[i]-a[i-1]>2*pre:
        pos=a[i-1]
        cnt=0
        tmppre=pre
        while pos+2*tmppre<a[i]:
            pos+=2*tmppre
            tmppre<<=1
            cnt+=1
        L,R=1,a[i]-a[i-1]-1
        while L<R:
            mid=L+R+1>>1
            if check(mid,cnt,a[i]-a[i-1],pre):L=mid
            else:R=mid-1
        pre=L
        ans+=cnt
        #print(a[i-1],a[i],ans,pre)
    else:pre=a[i]-a[i-1]
print(ans)
            
