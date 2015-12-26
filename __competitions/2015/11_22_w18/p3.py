"""
https://www.hackerrank.com/contests/w18/challenges/gg
From the very beginning it was clear that this is a combinatorial problem

First thing I have done was creating a bruteforce solution, which I used to find patterns.
After hopelessly searching for patterns I gave up. Started to use math but was able to find
formula only for strings of the form '0..01..1', which is combinations. Also it was clear that
changing 0s and 1s changes nothing. During this time I came up with idea to use islands of numbers
and to represent 00011011111 as [3, 2, 1, 5].

Started to search. The first thing I found was a https://en.wikipedia.org/wiki/Alternating_permutation
which later showed that I have to search for a 'number of permutations with a signature' which gave
me a couple of papers, majority of them were not useful

USED
http://arxiv.org/pdf/math/0607763.pdf Page 10

Related
http://arxiv.org/pdf/1008.1512.pdf  Page 7
http://oeis.org/A060351
http://www.emis.de/journals/INTEGERS/papers/m1/m1.pdf
http://www.sciencedirect.com/science/article/pii/S0012365X0000176X
http://www.emis.de/journals/INTEGERS/papers/m1/m1.pdf

Some interesting concepts
http://www.artofproblemsolving.com/wiki/index.php/Alternating_permutation
http://math2.uncc.edu/~hbreiter/m6105/snakes.pdf

Got a correct solution, which is way faster than bruteforce, but still too slow to pass.
"""
def bruteforce(s):
    from itertools import permutations
    def isValid(s, arr):
        for i in xrange(len(s)):
            if s[i] == "G":
                if arr[i] < arr[i + 1]:
                    return False
            else:
                if arr[i] > arr[i + 1]:
                    return False

        return True

    return sum(isValid(s, i) for i in permutations(range(len(s) + 1)))

# ==============

total = 0
def getIslands(s):
    islands, c, prev = [], 0, -1
    for i in s:
        if i == prev:
            c += 1
        else:
            if prev != -1:
                islands.append(c)
            c = 1
            prev = i

    islands.append(c)
    return islands

def C(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    result = 1
    for i in xrange(1, k + 1):
        result = result * (n - i + 1) / i
    return result

def recurse(islands):
    global total
    if len(islands) == 1:
        total += 1
        return
    elif len(islands) == 2:
        total += C(islands[0] + islands[1], islands[1])
        return

    for i in xrange(len(islands)):
        tmp = islands[:]
        tmp[i] -= 1
        if tmp[i] == 0:
            if i == 0:
                tmp = tmp[1:]
            elif i == len(tmp) - 1:
                tmp = tmp[:-1]
            else:
                tmp = tmp[:i - 1] + [tmp[i - 1] + tmp[i + 1]] + tmp[i + 2:]

        recurse(tmp)

s = "GGLGLGG"
islands = getIslands(s)
recurse(islands)

print total
print bruteforce(s)
