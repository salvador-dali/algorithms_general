# https://www.interviewbit.com/problems/rotated-sorted-array-search/
def findMin(A):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right)/2
        next = (mid+1) % len(A)
        prev = (mid+ len(A) -1) % len(A)
        if A[left] <= A[right]:
            return left
        elif A[mid] <= A[prev] and A[mid] <= A[next]:
            return mid
        elif A[mid] <= A[right]:
            right = mid - 1
        elif A[mid] >= A[left]:
            left = mid + 1
    return 0

def searchInRotated(arr, n):
    middle = findMin(arr)
    # print middle, arr[middle]
    # print arr[:middle]
    # print arr[middle:]
    if middle == 0:
        low, high = 0, len(arr)
    elif arr[0] < n:
        low, high = 0, middle - 1
    else:
        low, high = middle, len(arr) - 1
    # print low, high
    while low <= high:
        middle = (low + high) / 2
        val = arr[middle]
        if val == n:
            return middle

        if val > n:
            high = middle - 1
        else:
            low = middle + 1

    return -1


# arr = [36, 37, 40, 50, 60, 70, 0, 10, 20, 30, 31, 32, 33, 34, 35]
arr = [200, 205, 206, 207, 208, 0, 1, 7, 67, 133, 178, 198]
print searchInRotated(arr, 207)