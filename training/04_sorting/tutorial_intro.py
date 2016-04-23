# https://www.hackerrank.com/challenges/tutorial-intro
def binarySearch(arr, x):
    start, end = 0, len(arr)

    while start < end:
        middle = (start + end) / 2
        el = arr[middle]

        if el < x:
            start = middle + 1
        elif el > x:
            end = middle
        else:
            return middle

    return -1

n, _ = input(), raw_input()
print binarySearch(list(map(int, raw_input().split())), n)