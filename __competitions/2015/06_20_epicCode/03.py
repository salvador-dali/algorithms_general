_, diff = map(int, raw_input().split())
arr1 = list(map(int, raw_input().split()))
arr2 = list(map(int, raw_input().split()))
arr1.sort()
arr2.sort()
i, j, s = 0, 0, 0
while i != len(arr1) and j != len(arr2):
    if abs(arr1[i] - arr2[j]) <= diff:
        s += 1
        i += 1
        j += 1
    elif arr1[i] < arr2[j]:
        i += 1
    else:
        j += 1

print s
