N, D, K = map(int, raw_input().split())
days = [map(int, raw_input().split()) for i in xrange(N)]
d = [input() for i in xrange(K)]


from bisect import insort_left as insert
from bisect import bisect_left as find

def add_interval(arr, interval, d):
    days_num = interval[1] - interval[0]
    if days_num < d:
        return 0

    if not len(arr):
        arr.append(interval)
        return days_num

    pos, possible_positions = find(arr, interval), []
    if pos:
        possible_positions.append(arr[pos - 1])

    if pos < len(arr):
        possible_positions.append(arr[pos])

    if len(possible_positions) == 1:
        if not pos:
            if arr[0][0] < interval[1]:
                return 0
            elif arr[0][0] == interval[1]:
                arr[0][0] = interval[0]
                return days_num
            else:
                insert(arr, interval)
                return days_num

        if arr[-1][1] > interval[0]:
            return 0
        elif arr[-1][1] == interval[0]:
            arr[-1][1] = interval[1]
            return days_num
        else:
            insert(arr, interval)
            return days_num

    p1, p2 = possible_positions[0], possible_positions[1]
    if p1[1] > interval[0] or p2[0] < interval[1]:
        return 0
    elif p1[1] == interval[0] and p2[0] == interval[1]:
        p1[1] = p2[1]
        del arr[pos]
        return days_num
    elif p1[1] == interval[0]:
        p1[1] = interval[1]
        return days_num
    elif p2[0] == interval[1]:
        p2[0] = interval[0]
        return days_num
    else:
        insert(arr, interval)
        return days_num

def analyse(days, d):
    arr = []
    return sum(add_interval(arr, [r, l + 1], d) for r, l in days)

for el in d:
    print analyse(days, el)