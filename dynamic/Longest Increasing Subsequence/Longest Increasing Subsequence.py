# A naive Python implementation of LIS problem

""" To make use of recursive calls, this function must return
two things:
1) Length of LIS ending with element arr[n-1]. We use
max_ending_here for this purpose
2) Overall maximum as the LIS may end with an element
before arr[n-1] max_ref is used this purpose.
The value of LIS of full array of size n is stored in
*max_ref which is our final result """

# global variable to store the maximum
from importlib.resources import path


global maximum


def _lis(arr, n):

	# to allow the access of global variable
	global maximum

	# Base Case
	if n == 1:
		return 1

	# maxEndingHere is the length of LIS ending with arr[n-1]
	maxEndingHere = 1

	"""Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
	IF arr[n-1] is smaller than arr[n-1], and max ending with
	arr[n-1] needs to be updated, then update it"""
	for i in range(1, n):
		res = _lis(arr, i)
		if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
			maxEndingHere = res + 1

	# Compare maxEndingHere with overall maximum. And
	# update the overall maximum if needed
	maximum = max(maximum, maxEndingHere)

	return maxEndingHere


def lis(arr):

	# to allow the access of global variable
	global maximum

	# length of arr
	n = len(arr)

	# maximum variable holds the result
	maximum = 1

	# The function _lis() stores its result in maximum
	_lis(arr, n)

	return maximum


def lis_dy(arr):
    n = len(arr)
    L = [1 for _ in arr]
    mx = 0

    '''
    array: 10, 22, 9, 33, 21, 50, 41, 60
    + array size 1:
        -> len = 1 every in n elements
        10, 22, 9, 33, 21, 50, 41, 60
         1  1   1   1   1   1   1   1
    + array size n: left -> right
        10, 22, 9, 33, 21, 50, 41, 60
        1   2   1   3   2   4   4   5

    '''
    path = {}

    for i in range(len(arr)):
        path[i] = []
        path[i].append(arr[i])

    for i in range(1, n):
        for j in range(0, i):
            if (arr[j] < arr[i] and L[j] + 1 > L[i]):
                L[i] = L[j] + 1
                path[i].append(arr[j])
        path[i].append(arr[i])

    print("L: ", L)
    print("Mx: ", max(L))
    print("Path: ", path)

# Driver program to test the above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)
print ("Length of lis is ", lis(arr))
lis_dy(arr)

# This code is contributed by NIKHIL KUMAR SINGH
