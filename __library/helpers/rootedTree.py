# find the path from a root of a tree to the goal
def BFS(tree, root, goal):
    # if the goal is the root - return the path immediately
    if root == goal:
        return [root]

    # initializing the FIFO with the root element
    import Queue
    q = Queue.Queue()
    q.put((root, None))
    parent = None
    # and creating a backtracking hash
    backtrack = {}

    # expand our frontier while whe have not checked all potential elements
    while not q.empty():
        # taking the first element from the FIFO and put it in the backtracking hash
        node, prev = q.get()
        backtrack[node] = prev

        # if the element is not a leaf (has children)
        if node in tree:
            # check each child
            for child in tree[node]:
                # if it is a goal then break the loop (checking it here, allows to save additional round of iterations)
                if child == goal:
                    parent = node
                    break
                # it is not the goal, adds it to the FIFO
                q.put((child, node))

    # the goal can not be reached
    if parent is None:
        return None

    # generate the path from the backtracking
    path = [parent]
    while backtrack[parent] is not None:
        parent = backtrack[parent]
        path.append(parent)

    return path[::-1]

def numberOfChildrenForEveryNode(tree, root):
    from Queue import Queue
    # Finds the number of children (together with the node) for each node
    # takes a tree in the form {1: [2, 3], 2: [], 3: []}
    # uses BFS runs in O(V + E) and space O(V)
    frontier = Queue()
    frontier.put(root)
    checkedDistance = {root: 0} # dictionary of checked elements, together with the distance from the root
    listInc = []                # stores the list of nodes in the order they were expanded
    while not frontier.empty():
        node = frontier.get()
        listInc.append(node)
        for child in tree[node]:
            if child not in checkedDistance:    # this is not needed
                frontier.put(child)
                checkedDistance[child] = checkedDistance[node] + 1

    # iterate backwards with the list of nodes to calculate the number of children
    # this number is the sum of all previous children
    childrenNum = {}
    for element in listInc[::-1]:
        s = 1
        for i in tree[element]:
            s += childrenNum[i]
        childrenNum[element] = s

    return childrenNum