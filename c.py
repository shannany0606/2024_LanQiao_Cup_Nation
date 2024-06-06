ts="~!@#$%^&*()_"
T=int(input())
for _ in range(T):
    s=input()
    n=len(s)
    tag=1
    ex=[0]*3
    tsset=set()
    for c in s:
        if not c.isdigit() and not c.isalpha() and c not in ts:
            tag=0
            break
        if ord('A')<=ord(c)<=ord('Z'):ex[0]=1
        if ord('a')<=ord(c)<=ord('z'):ex[1]=1
        if c.isdigit():ex[2]=1
        if c in ts:tsset.add(c)
    if tag==0:
        print(0)
        continue
    if len(tsset)>=3 and sum(ex)>=2 and n>=12:print(3)
    elif sum(ex)+(1 if len(tsset) else 0)>=2 and n>=8:print(2)
    elif n>=6:print(1)
    else:print(0)


        
    
