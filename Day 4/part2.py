lines = [i.strip() for i in open("day4.in","r").readlines()]
t = sorted(["X","M","A","S"])
k = [list("MAS"),list("SAM")]
ans = 0
for i,v in enumerate(lines):
    for ii,vv in enumerate(v):
        try:
            if [lines[i][ii],lines[i+1][ii+1],lines[i+2][ii+2]]in k and [lines[i][ii+2],lines[i+1][ii+1],lines[i+2][ii]] in k:


                ans += 1
        except: pass


print(ans)
