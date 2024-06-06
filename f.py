ans=""
pos=0
n=0
T=int(input())
for _ in range(T):
    op=input()
    if op[0].isdigit():
        if op[-1]=='h':
            pos=max(0,pos-int(op[:-1]))
        else:
            pos=min(n,pos+int(op[:-1]))
    elif op[0]=='i':
        s=op[7:]
        s=s[1:-1]
        ans=ans[:pos]+s+ans[pos:]
        m=len(s)
        n+=m
        pos+=m
    else:
        m=int(op[1:-1])
        if op[-1]=='h':
            if pos<=m:
                ans=ans[pos:]
                n-=pos
                pos=0
            else:
                ans=ans[:pos-m]+ans[pos:]
                n-=m
                pos-=m
        else:
            if n-pos<=m:
                ans=ans[:pos]
                n=pos
            else:
                ans=ans[:pos]+ans[pos+m:]
                n-=m
    #print(ans,pos)
print(ans)

'''
9
d1h
insert ”hello”
insert ” world”
7h
d2h
insert ”11”
3l
d1l
insert ”0”
'''