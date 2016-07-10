class HuffmanCode:
    """
    Huffman code is a variable length encoding, which means that different symbols are encoded with different
    amount of bytes. It takes into advantage the fact that different symbols can have different frequencies.
    For any frequencies it produces optimal prefix-free encoding

    Important thing is that in order for a huffman code to be unambiguous, it should use prefix free encoding
    which means that none of the codes is a prefix of another one.

    So having an alphabet and a frequencies of each character, find the best encoding
    It is using down-up greedy approach and using a tree to encode everything
    Each edge is 1 or 0 and each vertex is one letter from the alphabet.
    Once we combine two elements {a, b} with {p_a and p_b} as their frequency we create
    another element {ab} with a frequency {p_a + p_b}.

    So the idea is to use merge two smallest elements and replacing them by a new one with the new probability.
    By using queues you end up in O(n log(n)) time

    There is even better approach to construct Huffman code. It runs in O(n) if the frequencies are sorted,
    yeah, with unsorted frequencies you will still end up with nlogn, but the constant is smaller.

    So here is the approach:
    You have two queues, q1 has the frequencies in non-decreasing order, and q2 is empty.
    While there is more then 1 element in both queues together, you do the following.
    - two times remove either element from q1, if q2 is empty, or element in q2 if q1 is empty or smaller
      from the left from one of the queues
    - add the sum to the second queue
    - add the element to the tree

    Example of usage:
    h = HuffmanCode([(5, 'a'), (7, 'b'), (10, 'c'), (15, 'd'), (20, 'e'), (45, 'f')])
    msg = 'abcadf'
    print msg == h.decode(h.encode(msg))
    """
    def __init__(self, frequencies):
        from collections import deque
        def helper(q1, q2):
            if not len(q1):
                return q2.popleft()
            elif not len(q2):
                return q1.popleft()

            return q1.popleft() if q1[0][0] <= q2[0][0] else q2.popleft()

        def dfs(tree, el, s):
            if el in tree:
                dfs(tree, tree[el][0], s + '0')
                dfs(tree, tree[el][1], s + '1')
            else:
                codingTable[el] = s

        # python uses timsort, which is O(nlogn) but if the input is sorted, it will run in O(n)
        frequencies.sort()
        q1, q2, tree = deque(frequencies), deque(), {}
        while len(q1) + len(q2) != 1:
            a, b = helper(q1, q2), helper(q1, q2)

            q2.append((a[0] + b[0], a[1] + b[1]))
            tree[a[1] + b[1]] = [a[1], b[1]]

        self.tree = tree
        self.root = a[1] + b[1]
        codingTable = {}
        dfs(tree, self.root, '')
        self.table = codingTable
        self.pref = {i[1]: i[0] for i in frequencies}

    def encode(self, message):
        return ''.join([self.table[i] for i in message])

    def decode(self, message):
        text, node = '', self.root
        for i in message:
            node = self.tree[node][int(i)]
            if node not in self.tree:
                text += node
                node = self.root

        return text

    def showStats(self):
        total = 0
        for i in self.table:
            print i, ':', self.table[i]
            total += self.pref[i] * len(self.table[i])
        print
        print 'Expected number of bits', total

