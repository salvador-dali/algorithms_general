# https://www.interviewbit.com/problems/bst-iterator/

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.populate_stack(root)

    def populate_stack(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        node = self.stack.pop()
        self.populate_stack(node.right)
        return node.val