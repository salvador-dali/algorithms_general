# https://www.hackerrank.com/challenges/quicksort3
def partition(array, lo, hi):
    pivot_index = hi
    pivot_value = array[pivot_index]
    store_index = lo

    for i in xrange(lo, hi):
        if array[i] <= pivot_value:
            array[i], array[store_index] = array[store_index], array[i]
            store_index += 1
    array[pivot_index], array[store_index] = array[store_index], array[pivot_index]
    return store_index


def quicksort(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        print(' '.join([str(i) for i in array]))
        quicksort(array, lo, p-1)
        quicksort(array, p+1, hi)


size = input()
quicksort(map(int, raw_input().split()), 0, size-1)