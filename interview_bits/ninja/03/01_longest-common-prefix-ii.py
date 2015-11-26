# https://www.interviewbit.com/problems/longest-common-prefix-ii
def calculate(arr, n):
    arr = [i[:n] for i in arr] + [-1]
    print arr
    prev, res, cnt = None, 0, 0
    for i in arr:
        if i == prev:
            cnt += 1
        else:
            prev = i
            if cnt:
                res += cnt * (cnt + 1) / 2
            cnt = 1

    return res


arr = ['acaa', 'acc', 'bbb', 'b', 'cca', 'bbc', 'ccc', 'babba', 'b']
print calculate(arr, 1)
