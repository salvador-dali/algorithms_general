# https://www.hackerrank.com/challenges/clique
# calculate the number of edges for a turan graph
# http://en.wikipedia.org/wiki/Tur%C3%A1n_graph
def turan(v, r):
    return (1 - 1.0/(r - 1)) * v**2 / 2

# gives the first approximation about the clique R
def approximation(v, e):
    res = float(v**2) / (v**2 - 2*e) + 1
    if res % 1:
        return int(res)

    return int(res) - 1

def minimumMaximumClique(v, e):
    r = approximation(v, e)
    for i in xrange(r, r + 4):
        print turan(v, i)
        if turan(v, i) >= e:
            return i - 1


#print test(19, 166)
#print turan(19, 13)

print minimumMaximumClique(19, 166)