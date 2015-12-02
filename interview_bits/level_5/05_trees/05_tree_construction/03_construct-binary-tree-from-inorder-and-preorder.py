# https://www.interviewbit.com/problems/construct-binary-tree-from-inorder-and-preorder/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def construct_inorder_preorder(arr_inorder, arr_preorder, pos_s, pos_e):
    if pos_s > pos_e:
        return None

    node = TreeNode(arr_preorder[construct_inorder_preorder.preorder_index])
    construct_inorder_preorder.preorder_index += 1

    if pos_s == pos_e:
        return node

    for inorder_pos in xrange(pos_s, pos_e + 1):
        if arr_inorder[inorder_pos] == node.val:
            break

    node.left = construct_inorder_preorder(arr_inorder, arr_preorder, pos_s, inorder_pos - 1)
    node.left = construct_inorder_preorder(arr_inorder, arr_preorder, inorder_pos + 1, pos_e)
    return node


arr_inorder = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
arr_preorder= ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']

construct_inorder_preorder.preorder_index = 0
n = construct_inorder_preorder(arr_inorder, arr_preorder, 0, len(arr_inorder) - 1)
print n.val


def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i

def buildTree(inOrder, preOrder, inStrt, inEnd):

    if (inStrt > inEnd):
        return None

    # Pich current node from Preorder traversal using
    # preIndex and increment preIndex
    tNode = TreeNode(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    # If this node has no children then return
    if inStrt == inEnd :
        return tNode

    # Else find the index of this node in Inorder traversal
    inIndex = search(inOrder, inStrt, inEnd, tNode.val)

    # Using index in Inorder Traversal, construct left
    # and right subtrees
    tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex-1)
    tNode.right = buildTree(inOrder, preOrder, inIndex+1, inEnd)

    return tNode