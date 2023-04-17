def balancedSums_sol_01(arr):
    # Write your code here
    brr = []
    for i in arr:
        if i != 0:
            brr.append(i)
        
    n = len(brr)
    if n <= 1:
        return "YES"
    
    left_sum = 0
    right_sum = 0
    left = 0
    right = n-1
    while left < right:
        
        if left_sum < right_sum:
            left_sum += brr[left]
            left += 1
        else:
            right_sum += brr[right]
            right -= 1
            
            
    if left_sum == right_sum:
        return "YES"
    return "NO"

def balancedSums(arr):
    
    sum_all = sum(arr)
    print(sum_all)
    
    temp_sum = 0
    for i in arr:
        if temp_sum == sum_all-i-temp_sum:
            return "YES"
        temp_sum += i
    
    return "NO"

arr = [0, 0, 2, 0]
print(balancedSums(arr))