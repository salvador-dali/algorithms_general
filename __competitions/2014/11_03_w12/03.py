# http://en.wikipedia.org/wiki/Topological_sorting
# https://www.hackerrank.com/contests/w12/challenges/favourite-sequence
def favourite(arr):
    h_normal, h_reversed, output = {}, {}, []
    # create a dictionary which maps the previous number to its previous value
    # for example [5, 2, 3] will create 3 -> [2] and 2 -> [5]
    for j in arr:
        if len(j) and j[0] not in h_normal:
            h_normal[j[0]] = set()
        for i in xrange(1, len(j)):
            if j[i] in h_normal:
                h_normal[j[i]].add(j[i - 1])
            else:
                h_normal[j[i]] = {j[i - 1]}

    # for a faster lookup you will need to create a reverse dictionary
    for i in h_normal:
        for j in h_normal[i]:
            if j not in h_reversed:
                h_reversed[j] = {i}
            else:
                h_reversed[j].add(i)

    while h_normal:
        # get the list of all the keys with an empty values, then select the smallest (for lexicographical ordering)
        # then remove the smallest one and remove the key from the dictionary
        empty = [v for v in h_normal if not len(h_normal[v])]
        while empty:
            empty.sort(reverse=True)
            e = empty.pop()
            output.append(e)
            del h_normal[e]
            if e in h_reversed:
                for i in h_reversed[e]:
                    h_normal[i].remove(e)
                    if not h_normal[i]:
                        empty.append(i)

    return output

arr = []
for i in xrange(input()):
    input()
    arr.append(list(map(int, raw_input().split())))

print ' '.join(map(str, favourite(arr)))