# https://www.interviewbit.com/problems/container-with-most-water/
def maxArea(arr):
    area, p1, p2 = 0, 0, len(arr) - 1
    while p1 < p2:
        area = max(area, min(arr[p1], arr[p2]) * (p2 - p1))
        if arr[p1] < arr[p2]:
            p1 += 1
        else:
            p2 -= 1

    return area

arr = [1, 7, 1, 1, 1, 1, 7]
print maxArea(arr)

