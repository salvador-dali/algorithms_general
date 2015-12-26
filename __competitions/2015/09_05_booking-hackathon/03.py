facilities = []
for _ in xrange(input()):
    t = raw_input().strip()
    facilities.append((t.lower(), t))

description= raw_input().lower()

res = [f[1] for f in facilities if f[0] in description]
res.sort()
for i in res:
    print i
