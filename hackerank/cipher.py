

def cipher_sol_01(k, s):
    # Write your code here
    n = len(s) - k + 1
    # print(n)
    res = s[0]
    # print(res)
    
    count_1 = 0
    for i in range(1,n):
        count_1 = 0
        for j in range(1,k):
            if i-j >= 0:
                temp = int(res[i-j])
                if temp == 1:
                    count_1 += 1
            else:
                break
            
        # print("----")
        # print("i: ", i)
        # print(res)
        # print("count_1: ", count_1)
        if count_1 % 2 == 0:
            if int(s[i]) == 1:
                res += "1"
            else:
                res += "0"
        else:
            if int(s[i]) == 1:
                res += "0"
            else:
                res += "1"
    
    return res

def cipher(k, s):
    # Write your code here
    n = len(s) - k + 1
    res = ""
    count_1 = 0
    
    for i in range(n):
        if i-k+1 > 0:
            if res[i-k] == "1":
                count_1 -= 1
        
        if count_1 % 2 == 0:
            if int(s[i]) == 1:
                res += "1"
                count_1 += 1
            else:
                res += "0"
        else:
            if int(s[i]) == 1:
                res += "0"
            else:
                res += "1"
                count_1 += 1
    
    return res

s = "1110100110"
k = 4

# s = "10001"
# k = 2

res = cipher(k, s)
print("---RES----")
print(res)