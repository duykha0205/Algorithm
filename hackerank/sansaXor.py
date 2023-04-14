

def sansaXor_helper(arr, k):
    
    if k == len(arr):
        res = arr[0]
        for i in range(1, len(arr)):
            res ^= i
        return res
    
    for x in arr:
        pass
    
    return 1

def sansaXor_sol_01(arr):
    
    # sub_arr = get_all_subarrays(arr)
    # res = sub_arr[0][0]
    # for x in sub_arr[1:]:
    #     for y in x:
    #         res ^= y
    
    res = None
    for start in range(len(arr)):
        for end in range(start + 1, len(arr) + 1):
            if res == None:
                res = arr[start:end][0]
            else:
                for i in arr[start:end]:
                    res ^= i
    
    return res

def get_all_subarrays(array):
    subarrays = []
    for start in range(len(array)):
        for end in range(start + 1, len(array) + 1):
            subarray = array[start:end]
            subarrays.append(subarray)
    return subarrays

def permutations_k_elements(items, perm=[], k=None, start=0):
    if len(perm) == k:
        print(perm)
        return perm
    else:
        for i in range(start, len(items)):
            perm.append(items[i])
            permutations_k_elements(items, perm, k, i+1)
            perm.pop()
            
            
def sansaXor(arr) -> int:
    n = len(arr)
    res = 0
    for i in range(n):
        freq = (i+1) * (n-i)
        if freq % 2 != 0:
            res ^= arr[i]
    return res

# arr = [4, 5, 7, 5]
arr = [3, 4, 5]
print(sansaXor(arr))
# permutations_k_elements(items=arr, k=1, start=0)