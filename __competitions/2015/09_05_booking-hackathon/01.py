speed = {'metro': 20, 'bike': 15, 'foot': 5}
places = [map(float, raw_input().split()) for _ in xrange(input())]  
hotels = []
for _ in xrange(input()):
    e = raw_input().split()
    hotels.append([float(e[0]), float(e[1]), speed[e[2]], int(e[3])])
    
from math import cos, asin, sqrt
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

for h in hotels:
    res = []
    for p in places:
        d = distance(h[0], h[1], p[1], p[2])
        d = round(d, 2)
        t = d / h[2] * 60
        if t <= h[3]:
            res.append((t, p[0]))

    res.sort()
    print ' '.join([str(int(i[1])) for i in res])