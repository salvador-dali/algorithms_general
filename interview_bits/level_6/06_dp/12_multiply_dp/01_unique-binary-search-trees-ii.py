# https://www.interviewbit.com/problems/unique-binary-search-trees-ii/
def catalan(n):
    prev = 1
    for i in xrange(n):
        prev = prev * 2 * (2 * i + 1) / (i + 2)
    return prev