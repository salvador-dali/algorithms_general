# https://www.interviewbit.com/problems/clone-graph/
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


def get_graph(node):
    going_to_check, already_checked = {node}, set()
    graph = {}
    while going_to_check:
        curr = going_to_check.pop()
        already_checked.add(curr)
        for i in curr.neighbors:
            if i not in already_checked:
                going_to_check.add(i)

        graph[curr.label] = [i.label for i in curr.neighbors]

    print graph

def clone_graph(G):
    nodes = {k: UndirectedGraphNode(k) for k in G}

    for k, v in G.iteritems():
        nodes[k].neighbors = [nodes[i] for i in v]

    for k in nodes:
        return nodes[k]

# ----------------------

from collections import deque
def cloneGraph(node):
    q, h = deque(), {node: UndirectedGraphNode(node.label)}
    q.append(node)
    while len(q) > 0:
        t = q[0]
        q.popleft()
        for i in t.neighbors:
            if i not in h:
                h[i] = UndirectedGraphNode(i.label)
                q.append(i)
            h[t].neighbors.append(h[i])

    return h[node]