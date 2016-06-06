from collections import Counter
def fast(arr, mod):
    arr, total = [i % mod for i in arr], len(arr)
    cnt = Counter(arr)

    to_sort, have_seen, total = [], set(), 0
    for k, v in cnt.iteritems():
        complementary = (mod - k) % mod
        if k == complementary:
            to_sort.append((1, k))
        else:
            to_sort.append((v, k))

    to_sort.sort(reverse=True)
    for v, k in to_sort:
        complementary = (mod - k) % mod
        if k not in have_seen:
            have_seen.add(k)
            have_seen.add(complementary)
            total += v

    return total

_, mod = map(int, raw_input().split())
arr = map(int, raw_input().split())
print fast(arr, mod)