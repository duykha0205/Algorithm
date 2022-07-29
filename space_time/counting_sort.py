

def countSort(arr):
    output = [0 for i in range(len(arr))]
    count = [0 for i in range(max(arr)+1)]

    for i in arr: count[i] += 1
    for i in range(1, max(arr)+1): count[i] += count[i-1]

    print(output)
    print(count)

    for i in range(len(arr)):
        print(count[arr[i]]-1, " - ", arr[i])
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    return output


# Driver program to test above function
arr = [8, 2, 3, 1, 5, 10, 57, 24]
ans = countSort(arr)
print(ans)

