"""
https://www.hackerrank.com/contests/w18/challenges/gg

Given a particular signature (up, down) find the number of permutations that satisfy this signature
here up = 1, down = 0. Example of a signature: [0, 1, 1, 1, 0, 1, 0, 1, 0, 1].

Runs in O(n^2)

- http://arxiv.org/pdf/math/0607763.pdf Page 10
- http://arxiv.org/pdf/1008.1512.pdf  Page 7
- http://oeis.org/A060351
- http://www.emis.de/journals/INTEGERS/papers/m1/m1.pdf
- http://www.sciencedirect.com/science/article/pii/S0012365X0000176X
- http://www.emis.de/journals/INTEGERS/papers/m1/m1.pdf

Partial case, where the signature is alternating: [0, 1, 0, 1, ...]
http://www.artofproblemsolving.com/wiki/index.php/Alternating_permutation
"""
def permutations_with_signature(signature):
    res = [1]
    for i in xrange(len(signature)):
        res2 = [0] * (i + 2)
        if signature[i] == 1:
            res = res[::-1]
        for j in xrange(i + 1):
            res2[j + 1] = res2[j] + res[j]
        if signature[i] == 1:
            res = res2[::-1]
        else:
            res = res2[:]

    return sum(res)


signature = [0, 1, 1, 1, 0, 1, 0, 1, 0, 1]
print permutations_with_signature(signature)