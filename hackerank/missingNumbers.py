def missingNumbers(arr, brr):
    # Write your code here
    dict_brr = {}
    for b in brr:
        if b not in dict_brr:
            dict_brr[b] = 1
        else:
            dict_brr[b] += 1
            
            
    for a in arr:
        dict_brr[a] -= 1
    
    # res = set()
    # print(arr)
    # for i in arr:
    #     print(i)
    #     if arr.count(i) != brr.count(i):
    #         # brr.remove(i)
    #         # print(arr)
    #         # brr.remove(i)
    #         res.add(i)
        
    # return list(res)
    res = [ i for i in dict_brr if dict_brr[i] != 0]
    print(res)
    res.sort()
    return res


arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
print(missingNumbers(arr, brr))