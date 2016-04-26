# https://www.hackerrank.com/challenges/sherlock-and-minimax
# if you will sort all the elements and then the maximum from minimum
# will be only on between the elements or on the sides of the interval
def minimax(arr, a, b):
    arr.sort()
    diff = [a]
    for i in xrange(1, len(arr)):
        tmp = (arr[i - 1] + arr[i]) / 2
        if a <= tmp <= b:
            diff.append(tmp)

    if diff[-1] != b:
        diff.append(b)

    maximum, element = -1, -1
    for i in diff:
        tmp = min([abs(j - i) for j in arr])
        if tmp > maximum:
            maximum, element = tmp, i

    return element

raw_input()
arr = list(map(int, raw_input().split()))
a, b = map(int, raw_input().split())
print minimax(arr, a, b)