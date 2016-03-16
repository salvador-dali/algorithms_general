# https://www.interviewbit.com/problems/nearest-smaller-element/

def nearestSmallest(arr):
    stack, res = [], []
    for i in arr:
        while len(stack) and stack[-1] >= i:
            stack.pop()

        if len(stack) == 0:
            res.append(-1)
        else:
            res.append(stack[-1])

        stack.append(i)
    return res


arr = [34, 35, 27, 42, 5, 28, 39, 20, 28]
print nearestSmallest(arr)