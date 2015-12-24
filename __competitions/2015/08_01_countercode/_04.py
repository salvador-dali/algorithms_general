# checking bruteforce
def attempt(arr):
    return [arr[0]] + [arr[i] for i in xrange(1, len(arr)) if arr[i] <= arr[i - 1]]

def main(arr):
    if arr[0] < arr[1] and all(arr[i] > arr[i+1] for i in xrange(1, len(arr)-1)):
        return len(arr) - 1
    res, t = arr, 0
    while True:
        res1 = attempt(res)
        if len(res) == len(res1):
            return t
        res = res1
        t += 1

input()
arr = list(map(int, raw_input().split()))
print main(arr)