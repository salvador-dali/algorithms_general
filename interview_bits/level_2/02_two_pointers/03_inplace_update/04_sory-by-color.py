# https://www.interviewbit.com/problems/sory-by-color/
def sorting(arr):
    tmp = [0] * 3
    for i in arr:
        tmp[i] += 1

    return [0] * tmp[0] + [1] * tmp[1] + [2] * tmp[2]