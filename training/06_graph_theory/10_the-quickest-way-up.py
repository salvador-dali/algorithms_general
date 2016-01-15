# https://www.hackerrank.com/challenges/the-quickest-way-up
# create a graph from the board and then use BFS to find the best path from start to end

import Queue
def snakes_ladders(ladders, snakes):
    # constructs a graph from the information from the puzzle
    maxSquare = 100
    graph = {i: [j for j in xrange(i + 1, min(i + 7, maxSquare + 1))] for i in xrange(1, maxSquare + 1)}

    for a, b in ladders:
        graph[a].append(b)

    for a, b in snakes:
        graph[a].append(b)

    # then just a simple BFS to find the shortest path.
    # store the number of steps needed
    frontier = Queue.Queue()     # element and how many steps it took to go to this element
    checked = {}
    frontier.put([1, 0])
    while not frontier.empty():
        current, steps = frontier.get()
        if current == maxSquare:
            return steps - 1

        children = graph[current]
        for i in children:
            if i not in checked:
                frontier.put((i, steps + 1))

        checked[current] = 1

def convert(s):
    arr = []
    for i in s.split():
        arr.append(map(int, i.split(',')))
    return arr

l = '22,54'
s = '79,17 67,7 89,25 69,23'

print snakes_ladders(convert(l), convert(s))