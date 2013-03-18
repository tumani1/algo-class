# coding: utf-8

from sys import maxint as max_int
from time import time

def inver_On2(arr, inver = 0):
    arr = list(arr)
    arr_len = len(arr)

    if arr_len < 2:
        return arr, inver

    for i in range(0, arr_len - 1):
        for j in range(i + 1, arr_len):
            if arr[i] > arr[j]:
                inver += 1

    return arr, inver

def mergeSort(arr, inver = 0):
    arr = list(arr)
    arr_len = len(arr)

    if arr_len < 2:
        return arr, inver

    middle = arr_len // 2

    left, inver_left = mergeSort(arr[:middle])
    right, inver_right = mergeSort(arr[middle:])

    result, inver = merge(left + [max_int], right + [max_int])
    inver += inver_left + inver_right

    return result, inver

def merge(left, right):
    result = []
    len_left = len(left) - 1
    i = j = inver = 0

    while (left[i] != max_int or right[j] != max_int):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inver += len_left - i

    return result, inver

def main():
    # Start time
    start = time()

    # Inicialization
    arr_file = []

    # Open file
    f = open('IntegerArray.txt', 'r')
    for line in f: arr_file.append(int(line))
    f.close()

    # Sorting
    arr_file, inver = mergeSort(arr_file)
    print 'Count comparison in merge sort: %d' % inver

    print 'Elapsed Time: %s' % (time() - start)

if __name__ == '__main__':
    main()
