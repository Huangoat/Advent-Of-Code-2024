lines = [i.strip() for i in open("day7.in","r").readlines()]
def poss(target, nums, k, prev):
    if k>target and nums:
        return 0
    if not nums:
        if k==target: return 1
        return 0
    a = nums[0]
    l = poss(target, nums[1:], k+a, a)
    ll = poss(target, nums[1:], k*a, a)

    lll = poss(target, nums[1:], int(str(k)+str(a)), a)

    return l+ll+lll



#lines = ["3267: 81 40 27"]
ans = 0
for i,v in enumerate(lines):
    target, n = v.split(": ")
    target = int(target)
    nums = list(map(int, n.split()))
    
    if len(nums)==1:
        if target == nums[0]:
            ans += 1
            continue
        continue
    f = nums[0]
    #del nums[0]
    aa = poss(target, nums,0,f)
    if aa>0:
        ans += target

print(ans)
