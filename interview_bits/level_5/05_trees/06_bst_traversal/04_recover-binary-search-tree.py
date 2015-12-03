# https://www.interviewbit.com/problems/recover-binary-search-tree/
class Solution:
    def f(self, root):
        if root.left:
            self.f(root.left)
        if self.prev is not None:
            if root.val < self.prev.val:
                self.p2 = root
                if self.p1 is None:
                    self.p1 = self.prev
                
        self.prev = root
        if root.right:
            self.f(root.right)
            
    def recoverTree(self, A):
        self.prev = None
        self.p1 = None
        self.p2 = None
        self.f(A)
        return [self.p2.val, self.p1.val]