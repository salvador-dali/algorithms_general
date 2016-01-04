# https://www.hackerrank.com/challenges/correctness-invariant
def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i
        key = l[i]
        while (l[j - 1] > key) and (j > 0):
            l[j] = l[j - 1]
            j -= 1
            l[j] = key


m = input()
arr = map(int, raw_input().split())
insertion_sort(arr)
print " ".join(map(str, arr))