# https://www.hackerrank.com/challenges/countingsort4

arr = []
for i in xrange(int(raw_input())):
    a, b = raw_input().split()
    arr.append([int(a), b, i])

# just sort the list based on the 2 columns
arr = sorted(arr, key = lambda x : (x[0], x[2]))
l = len(arr) / 2
out = []
for i in arr:
    if i[2] < l:
        out.append('-')
    else:
        out.append(i[1])

print ' '.join(out)