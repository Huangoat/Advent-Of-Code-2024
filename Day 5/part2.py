lines = [i.strip() for i in open("day5.in","r").readlines()]
#before
d = {}
for k in lines:
    a, b= k.split("|")
    if a in d:
        d[a].append(b)
    else:
        d[a] = [b]



updates = [i.strip() for i in open("day5p2.in","r").readlines()]

ans = 0
 
updates = [[i for i in i.split(",")] for i in updates]



def check(v):
    for ii,vv in enumerate(v):
        for iii,vvv in enumerate(v):
            
            if iii<=ii: continue
            if vv in d:
                if vvv not in d[vv]:
                    v[ii],v[iii] = v[iii], v[ii]
                    return check(v)
                pass
            if vvv in d:
                if vv in d[vvv]:
                    v[ii],v[iii] = v[iii], v[ii]
                    return check(v)
    return v
