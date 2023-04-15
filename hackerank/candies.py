def candies_1(n, arr):
    # Write your code here
    
    i = 0
    c = 1
    res = 0
    while i < n-1:
        temp = i
        print("i: ", i)
        while i+1 < n and arr[i] < arr[i+1]:
            c += 1
            i += 1
            res -= 1
            
        res += c * (c+1) / 2
        c = 1
        
        print("c: ", c) 
        print("res: ", res)
        
        while i+1 < n and arr[i] > arr[i+1]:
            c += 1
            i += 1
            res -= 1
            
        res += c * (c+1) / 2
        c = 1   
        print("c: ", c) 
        print("res: ", res) 
        
        if i+1 < n and arr[i] == arr[i+1]:
            res += 1
            c = 1
            i += 1
        
            
    return int(res)

def candies(n, arr):
    # Write your code here
    res = [ 1 for _ in range(n)]
    
    for i in range(0, n-1):
        
        if (arr[i] < arr[i+1]):
            # print()
            # print("i: ", arr[i])
            # print("i+1: ", arr[i+1])
            if res[i] >= res[i+1]:
                # print()
                # print(arr[i])
                # print(arr[i+1])
                res[i+1] = res[i] + 1
                
    for i in range(n-1, 0, -1):
        if (arr[i] < arr[i-1]):
            if res[i] >= res[i-1]:
                res[i-1] = res[i] + 1
    
    # print(res)
    
    return sum(res)


# n = 3
# arr = [1,2,2]

n = 10
arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
print("candies", candies(n, arr))