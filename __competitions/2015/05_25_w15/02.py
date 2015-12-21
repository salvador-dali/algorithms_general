from Queue import PriorityQueue

def solve(elements):
    maximum, q = 0, PriorityQueue()
    for a, b in elements:
        q.put((b, a))
        while not q.empty() and q.queue[0][0] + 1 < len(q.queue):
            q.get()

        if len(q.queue) > a:
            maximum = max(maximum, len(q.queue))

    return maximum

arr = [tuple(map(int, raw_input().split())) for _ in xrange(int(input()))]
print solve(sorted(arr))