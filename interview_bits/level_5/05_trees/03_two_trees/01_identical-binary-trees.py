# https://www.interviewbit.com/problems/identical-binary-trees/
def is_identical(n1, n2):
    if n1 is None and n2 is None:
        return True
    
    if (n1 is None and n2 is not None) or (n2 is None and n1 is not None):
        return False

    return n1.val == n2.val and is_identical(n1.left, n2.left) and is_identical(n1.right, n2.right)