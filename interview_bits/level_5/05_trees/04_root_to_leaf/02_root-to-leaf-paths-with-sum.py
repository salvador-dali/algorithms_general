# https://www.interviewbit.com/problems/root-to-leaf-paths-with-sum/

def solution(node, num):
    results = []
    def path_sum(node, num, arr):
        if node is None:
            return

        if num == node.val and node.left is None and node.right is None:
            results.append(arr + [num])
            return

        return path_sum(node.left, num - node.val, arr + [node.val]) or path_sum(node.right, num - node.val, arr + [node.val])

    path_sum(node, num, [])
    return []