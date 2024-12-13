lines = [i.strip() for i in open("day3.in","r").readlines()]

ans = 0
do = True
for line in lines:
    for i,v in enumerate(line):

        try:
            if line[i:i+4]=="do()": do = True
        except:pass
        try:
            if line[i:i+7] == "don't()": do = False
        except: pass


        try:
            if not(line[i]=="m" and line[i+1]=="u" and line[i+2]=="l" and line[i+3]=="("):
                continue
            closebrac = False
            for ii,vv in enumerate(line):
                if vv==")" and ii>i:
                    closebrac = ii
                    break
            if not closebrac: continue
            to_test = line[i:closebrac+1]
            if to_test.count(",") != 1: continue
            brac_ind = i+to_test.index(",")
            l,r = line[i+4:brac_ind], line[brac_ind+1:closebrac]
            #print(l,r)
            if len(l)>3 or len(r)>3: continue
            try:
                if do:
                    print(int(l), int(r), int(l)*int(r))
                    ans += int(l)*int(r)
                else:
                    #do = True
                    continue
            except:
                pass


        except: print("index")

print(ans)

