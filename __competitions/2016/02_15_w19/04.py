def analysis(arr):
    from collections import defaultdict
    arr = [0] * 40
    m = defaultdict(int)
    for a in xrange(len(arr)):
        for b in xrange(a, len(arr)):
            for c in xrange(b + 1, len(arr)):
                for d in xrange(c, len(arr)):
                    m[(a, b)] += 1
                    m[(c, d)] += 1

    t = defaultdict(list)
    for i in sorted(m.keys()):
        t[i[0]].append(m[i])
    for i in xrange(len(arr)):
        print i, t[i][::-1] # each element x^2 / 2 - x / 2 + first element here

def bruteforce(arr):
    ans = 0
    for a in xrange(len(arr)):
        for b in xrange(a, len(arr)):
            el1 = min(arr[a:b + 1])
            for c in xrange(b + 1, len(arr)):
                for d in xrange(c, len(arr)):
                    ans += min(el1, min(arr[c:d + 1]))
    return ans

def attempt2(arr):
    from collections import defaultdict
    m = defaultdict(int)
    ans = 0
    for a in xrange(len(arr)):
        for b in xrange(a, len(arr)):
            for c in xrange(b + 1, len(arr)):
                for d in xrange(c, len(arr)):
                    v = min(min(arr[a:b + 1]), min(arr[c:d + 1]))
                    # print (a, b), (c, d), '\t', v, '\t', arr[a:b + 1], arr[c:d + 1]
                    ans += v
                    m[v] += 1

    res = []
    for i in sorted(m.keys()):
        # print i, m[i]
        res.append(m[i])

    return res

def stupid(arr):
    arr.sort(reverse=True)
    val = 0
    for i in xrange(1, len(arr)):
        val += arr[i] * i * (i + 1) * (i + 2) / 6
    print val

arr = [6, 2, 3, 1]
for i in xrange(len(arr)):
    for j in xrange(i, len(arr)):
        print min(arr[i:j + 1])



# Description of k is confusing.
#
# For test case 1: n=3 and k=5, k is the list of permutations having maximal distance has at least k elements. In which, we are considering 6 permutations having distance 1. Note that in this case, there is no permuation whose distance is 5
#
# For the second test case: n=4 and k=2, k is not used as at least k elements; but k is used as at least k distance. It seems conflicting with case 1. For case 2, we have following permutations:
#
# distance 1 permutations count : 22
# distance 2 permutations count : 02
#
# For k=2, there should be 2nd set (from distance 1 permuations) 1 2 4 3
#
# All Permutations of case 2 are as below:
#
# P01 1 2 3 4 distance is 1
# P02 1 2 4 3 distance is 1
# P03 1 3 2 4 distance is 1
# P04 1 3 4 2 distance is 1
# P05 1 4 2 3 distance is 1
# P06 1 4 3 2 distance is 1
# P07 2 1 3 4 distance is 1
# P08 2 1 4 3 distance is 1
# P09 2 3 1 4 distance is 1
# P10 2 3 4 1 distance is 1
# P11 2 4 1 3 distance is 2
# P12 2 4 3 1 distance is 1
# P13 3 1 2 4 distance is 1
# P14 3 1 4 2 distance is 2
# P15 3 2 1 4 distance is 1
# P16 3 2 4 1 distance is 1
# P17 3 4 1 2 distance is 1
# P18 3 4 2 1 distance is 1
# P19 4 1 2 3 distance is 1
# P20 4 1 3 2 distance is 1
# P21 4 2 1 3 distance is 1
# P22 4 2 3 1 distance is 1
# P23 4 3 1 2 distance is 1
# P24 4 3 2 1 distance is 1

