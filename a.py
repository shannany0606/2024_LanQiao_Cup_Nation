a=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
ans=0
for i in range(9):
    for j in range(i+1,9):
        if a[i][0]==a[j][0] or a[i][1]==a[j][1]:continue
        k=(a[i][1]-a[j][1])/(a[i][0]-a[j][0])
        b=a[i][1]-a[i][0]*k
        tag=1
        for o in range(9):
            if o==i or o==j:continue
            if a[o][1]==k*a[o][0]+b:
                tag=0
                break
        ans+=tag
        if tag:print(a[i],a[j])
print(ans)#12