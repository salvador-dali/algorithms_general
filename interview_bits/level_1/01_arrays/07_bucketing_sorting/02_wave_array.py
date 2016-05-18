# https://www.interviewbit.com/problems/wave-array/

def wave(arr):
    arr.sort()
    for i in xrange(len(arr) / 2):
        arr[2 * i], arr[2 * i + 1] = arr[2 * i + 1], arr[2 * i]

    return arr
