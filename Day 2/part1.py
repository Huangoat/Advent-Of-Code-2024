lines = [i.strip() for i in open("day2.in","r").readlines()]
ans = 0
for i in lines:
    k = list(map(int, i.split()))
    d = False
    if k[0] < k[1]: d = False
    else: d = True
    yes = True
    for ii,vv in enumerate(k):
        if ii==0: continue
        if abs(k[ii] - k[ii-1]) not in [1,2,3]: yes = False; break
        if k[ii] > k[ii-1] and d: yes = False; break
        if k[ii] < k[ii-1] and not d: yes = False; break
    if yes:
        ans += 1


print(ans)
