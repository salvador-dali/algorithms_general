hotels = []
for _ in xrange(input()):
    e = raw_input().split()
    hotels.append((int(e[0]), int(e[1]), set(e[2:])))

people = []
for _ in xrange(input()):
    e = raw_input().split()
    people.append((int(e[0]), set(e[1:])))
    
    
for p in people:
    goodHotels = [(len(h[2]), h[1], h[0]) for h in hotels if p[0] >= h[1] and p[1].issubset(h[2])]
    goodHotels.sort(key=lambda x: (-x[0], x[1], x[2]))
    print ' '.join([str(i[-1]) for i in goodHotels])