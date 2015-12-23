from itertools import chain, combinations
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def analyse(elements, ones):
    if not len(elements):
        return 0

    union = reduce(set.union, elements)
    if union != ones:
        return 0

    l = len(ones)
    return sum(1 for i in powerset(elements) if i and len(reduce(set.union, i)) == l)

N, M = map(int, raw_input().split())
people = [map(int, list(raw_input())) for i in xrange(N)]
need = list(map(int, list(raw_input())))

zeros = set(i + 1 for i in xrange(M) if not need[i])
ones = set(i + 1 for i in xrange(M) if need[i])

elements = []
for person in people:
    s = set(i + 1 for i in xrange(M) if person[i])
    if not len(s & zeros):
        elements.append(s)
    
print analyse(elements, ones)