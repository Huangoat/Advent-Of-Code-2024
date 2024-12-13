lines = [i.strip() for i in open("Day1.in","r").readlines()]
right, left = [], []
for i in lines:
    a,b = list(map(int, i.split()))
    right.append(a)
    left.append(b)

ans = 0
right, left = sorted(right), sorted(left)
for i,v in enumerate(right):
    ans += v * left.count(v)

print(ans)



