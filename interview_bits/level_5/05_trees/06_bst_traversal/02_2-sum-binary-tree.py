# https://www.interviewbit.com/problems/2-sum-binary-tree/
def generate_small(node):
    if node is None:
        for key in generate_small(node.left):
            yield key
        yield node
        for key in generate_small(node.right):
            yield key

def generate_big(node):
    if node is None:
        for key in generate_big(node.right):
            yield key
        yield node
        for key in generate_big(node.left):
            yield key

def find_sum(node, k):
    small, big = generate_small(node), generate_big(node)
    e1, e2 = next(small), next(big)
    while True:
        if e1.val + e2.val == k:
            if e1 != e2:
                return True
        elif e1.val + e2.val < k:
            try:
                e1 = next(small)
            except StopIteration:
                return False
        else:
            try:
                e2 = next(big)
            except StopIteration:
                return False

    return False


def is_true(node, k):
    res = []
    def get_all(node):
        if node is None:
            return

        get_all(node.left)
        res.append(node.val)
        get_all(node.right)

    get_all(node)
    h = {res[i]: i for i in xrange(len(res))}
    for i in xrange(len(res)):
        v2 = k - res[i]
        if v2 in h and [v2] != i:
            return True
    return False

