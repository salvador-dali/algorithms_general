# https://www.interviewbit.com/problems/3-sum/
def threeSumClosest(num, target):
    num.sort()
    diff, n = float("infinity"), len(num)
    for i in range(n - 2):
        begin, end = i + 1, n - 1
        while begin < end:
            if abs(num[i] + num[begin] + num[end] - target) < diff:
                diff = abs(num[i] + num[begin] + num[end] - target)
                res = num[i] + num[begin] + num[end]

            if num[i] + num[begin] + num[end] > target:
                end -= 1
            else:
                begin += 1
    return res
