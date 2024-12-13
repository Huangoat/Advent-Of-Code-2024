lines = [list(i.strip()) for i in open("day8.in","r").readlines()]

antinodes = set()

for i,v in enumerate(lines):
    for ii,vv in enumerate(v):
        if vv!=".":
            for a,b in enumerate(lines):
                for aa,bb in enumerate(b):
                    if (a,aa) == (i,ii): continue
                    poss = []
                    if vv!=bb: continue
                    if (i-a)%3 == 0 and (ii-aa)%3==0:
                        mx = min(i, a)
                        my = min(ii,aa)
                        poss.append((  mx+2*abs(i-a)//3, my+2*abs(ii-aa)//3 ))

                    xta, yta = 0,0
                    if i>a:
                        xta = i+(i-a)
                    else:
                        xta = i-(a-i)
                    if ii>aa:
                        yta = ii+(ii-aa)
                    else:
                        yta = ii-(aa-ii)

                    poss.append((xta,yta))


                    for x, y in poss:
                        if x>=0 and x<=len(lines)-1 and y>=0 and y<=len(lines[0])-1:
                            antinodes.add((x,y))
                    #print(poss)
#for x,y in antinodes:
#    lines[x][y] = "#"
#
#for i in lines:
#    print("".join(i))

print(len(antinodes))






