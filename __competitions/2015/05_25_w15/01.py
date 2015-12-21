sud = {1, 2, 3, 4, 5, 6, 7, 8, 9}
arr = range(1, 10)

def printRes(a, b, c, d):
    print '(' + str(a) + ',' + str(b) + ')' + ' <-> ' + '(' + str(c) + ',' + str(d) + ')'

def solve(s):
    br1, bre1, br2, bre2, bc1, bce1, bc2, bce2 = 0, 0, 0, 0, 0, 0, 0, 0
    for r in arr:
        rs = set(s[r-1])
        if rs != sud:
            if br1:
                br2, bre2 = r, list(sud-rs)[0]
            else:
                br1, bre1 = r, list(sud-rs)[0]

        cs = set()
        for c in arr:
            cs.add(s[c-1][r-1])
        if cs != sud:
            if bc1:
                bc2, bce2 = r, list(sud-cs)[0]
            else:
                bc1, bce1 = r, list(sud-cs)[0]

    if br1 == 0 and bc1 == 0 :
        print 'Serendipity'
        return

    if br2 != 0 and bc2 != 0 :
        l = sorted([(br1,bc1 if bre1 == bce1 else bc2), (br2,bc2 if bre2 == bce2 else bc1)])
        printRes(l[0][0], l[0][1], l[1][0], l[1][1])
        return

    if not bc1:
        for c in arr:
            if s[br1-1][c-1] == bre2 and s[br2-1][c-1] == bre1 :
                rr, cc, ss = (br1-1)/3, (c-1)/3, set()
                for t in xrange(3) :
                    ss |= set(s[3*rr+t][3*cc:3*(cc+1)])
                if (br1-1)/3 == (br2-1)/3 or ss != sud :
                    l = sorted([(br1,c), (br2,c)])
                    printRes(l[0][0], l[0][1], l[1][0], l[1][1])

        return
    if not br1:
        for r in arr:
            if s[r-1][bc1-1] == bce2 and s[r-1][bc2-1] == bce1 :
                cc, rr, ss = (bc1-1)/3, (r-1)/3, set()
                for t in xrange(3) :
                    ss |= set(s[3*rr+t][3*cc:3*(cc+1)])
                if (bc1-1)/3 == (bc2-1)/3 or ss != sud :
                    l = sorted([(r,bc1), (r,bc2)])
                    printRes(l[0][0], l[0][1], l[1][0], l[1][1])

for i in xrange(input()):
    print 'Case #' + str(i + 1) + ':'
    solve([[int(_) for _ in raw_input().split()] for j in xrange(9)])