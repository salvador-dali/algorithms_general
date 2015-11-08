# https://www.interviewbit.com/problems/rod-cutting/
# http://www.geeksforgeeks.org/dynamic-programming-set-13-cutting-a-rod/

def rod_cutting(arr):
    best_price = [arr[0]] + [0] * (len(arr) - 1)

    for val in xrange(1, len(arr)):
        m = 0
        for i in xrange((val + 3) / 2):
            if i == 0:
                m = max(m, arr[val - i])
            else:
                m = max(m, best_price[i - 1] + best_price[val - i])
        best_price[val] = m

    return best_price[-1]

def rod_cutting_shorter(arr):
    best_price = [arr[0]] + [0] * (len(arr) - 1)

    for val in xrange(1, len(arr)):
        best_price[val] = max(arr[val - i] if i == 0 else best_price[i - 1] + best_price[val - i] for i in xrange((val + 3) / 2))

    return best_price[-1]
