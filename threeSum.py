def threeSum(nums):

    res = []
    n,p,z = [],[],[]
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)

    N, P = set(n), set(p)
    if z:
        for num in P:
            if -1*num in N:
                res.append([-1*num,0, num])

    if len(z) >= 3:
        res.append([0,0,0])

    for i in range(len(n)):
        for j in range(i+1, len(n)):
            target = -1*(n[i]+n[j])
            if target in P:
                a = sorted([n[i], n[j], target])
                if a not in res:
                    res.append(a)

    for i in range(len(p)):
        for j in range(i+1, len(p)):
            target = -1*(p[i]+p[j])
            if target in N:
                a = sorted([p[i],p[j], target])
                if a not in res:
                    res.append(a)
    return res