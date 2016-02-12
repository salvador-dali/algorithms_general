# https://www.hackerrank.com/challenges/sherlock-and-pairs
# given the array of integers, calculate the number
# of pairs of indexes where A[i] == A[j] and i != j
def sameElements(arr):
    # save all into the hash to get the number of each character
    h = {}
    for i in arr:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1

    # if the character was selected n times, the pair of indexes is n*(n-1)
    s = 0
    for i in h:
        s += h[i] * (h[i] - 1)

    return s

for i in xrange(int(raw_input())):
    raw_input()
    arr = list(map(int, raw_input().split()))
    print sameElements(arr)