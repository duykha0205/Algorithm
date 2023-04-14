def getMinimumCost(k, c):
    
    res = 0
    n = len(c)
    
    if k == n:
        return sum(c)
    
    pos = n - 1
    turn = 1
    while pos >= 0:
        for i in range(k):
            if pos-i >= 0:
                res += turn * c[pos-i]
                # print(str(pos-i) + " " + str(i) + " " + str(res))
                
        pos -= k
        turn += 1
    
    return res


k = 2
c = [1,2,3]
# 2*1 + 1*2 + 3
print(getMinimumCost(k, c))