def expected(t_s, p_s):
    s, p = 0, 1
    for i in xrange(len(t_s)):
        s += t_s[i] * p
        p *= p_s[i]

    return s

def bestValue(times, probs):
    arr = []
    for i in xrange(len(probs)):
        if probs[i] == 1:
            arr.append((times[i], probs[i], float("-inf")))
        else:
            arr.append((times[i], probs[i], times[i] / (1 - probs[i])))

    arr.sort(key=lambda x: x[2])
    t, p, k = zip(*arr)
    return expected(t, p)

times, probs = [], []
for i in xrange(input()):
    a, b = map(float, raw_input().split())
    times.append(a)
    probs.append(b)
    
print bestValue(times, probs)