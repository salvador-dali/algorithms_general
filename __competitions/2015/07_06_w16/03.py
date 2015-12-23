def waterFlower(flowers, n, m, s, q) :
    if len(flowers) == 2:
        return [[1, 0], [flowers[1]]]

    beg, end, minimum, cost = 0, 0, float('inf'), 0
    for i in xrange(1, n):
        cost += q
        current, add, count = 0, 1, 0
        while add <= n:
            ss = add + i
            if ss > n:
                ss = n
            if flowers[ss] <= current:
                break
            count += 1
            current = flowers[ss]
            add = current+i+1
            if add > n and minimum > s*count+cost:
                minimum, beg, end = s*count+cost, count, i
                
    if n == m and minimum > n*s:
        beg, end = n, 0
        
    if beg == n:
        return [[beg, end], range(1, n + 1)]
    
    current, add, out = 0, 1, []
    while add <= n:
        ss = add+end
        if ss > n:
            ss = n
        if flowers[ss] <= current:
            break
        out.append(flowers[ss])
        current = flowers[ss]
        add = current+end+1
    return [[beg, end], out]

for _ in xrange(input()):
    N, M, S, Q = map(int, raw_input().split())
    flowers, value, i = [0]*(N+1), 0, 0
    for f in map(int, raw_input().split()):
        i += 1
        while i < f:
            flowers[i] = value
            i += 1
        flowers[f], value = f, f

    i = value+1
    while i <= N:
        flowers[i] = value
        i += 1
    a, b = waterFlower(flowers, N, M, S, Q)
    print " ".join(map(str, a))
    print " ".join(map(str, b))