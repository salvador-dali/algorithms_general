# https://www.interviewbit.com/problems/populate-next-right-pointers-tree/
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def next_pointer(root):
    curr_level, next_level = [root], []
    while curr_level:
        for i in xrange(len(curr_level) - 1):
            curr_level[i].next = curr_level[i + 1]

        for node in curr_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        curr_level, next_level = next_level[::], []
    return root
