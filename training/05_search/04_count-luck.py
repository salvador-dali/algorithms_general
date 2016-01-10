# https://www.hackerrank.com/challenges/count-luck
import Queue
def findStart(arr):
    for i in xrange(len(arr)):
        pos = arr[i].find('M')
        if pos != -1:
            return pos, i

def BFS(arr, x, y):
    w, h = len(arr[0]), len(arr)
    checked = {}                # dictionary of (x, y) coordinates, which we already checked
    frontier = Queue.Queue()    # (x, y, turns) location of the point with a number of turns done already
    frontier.put((x, y, 0))
    while not frontier.empty():
        x, y, turns = frontier.get()
        if arr[y][x] == '*':
            return turns

        checked[(y, x)] = 1
        moves = []
        if x + 1 < w and (y, x + 1) not in checked and arr[y][x + 1] != 'X':
            moves.append((x + 1, y))    # add RIGHT
        if x - 1 >= 0 and (y, x - 1) not in checked and arr[y][x - 1] != 'X':
            moves.append((x - 1, y))    # add LEFT
        if y + 1 < h and (y + 1, x) not in checked and arr[y + 1][x] != 'X':
            moves.append((x, y + 1))    # add DOWN
        if y - 1 >= 0 and (y - 1, x) not in checked and arr[y - 1][x] != 'X':
            moves.append((x, y - 1))    # add UP

        if len(moves) > 1:
            for i in moves:
                frontier.put((i[0], i[1], turns + 1))
        elif len(moves) == 1:
            frontier.put((moves[0][0], moves[0][1], turns))

def count_luck(arr):
    start = findStart(arr)
    return BFS(arr, start[0], start[1])

for i in xrange(input()):
    a, b = map(int, raw_input().split())
    arr = [raw_input() for j in xrange(a)]
    if count_luck(arr) == input():
        print 'Impressed'
    else:
        print 'Oops!'