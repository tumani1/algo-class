# coding: utf-8

from time import time

def partition(arr, left, right):
    pivot = arr[left]
    i = left + 1

    for j in range(i, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[left], arr[i - 1] = arr[i - 1], arr[left]
    return i - 1

def quickSortA(arr, left, right, count = 0):
    arr = list(arr)
    if left >= right - 1:
      return arr, count

    count = right - left - 1
    part = partition(arr, left, right)
    arr, count_left = quickSortA(arr, left, part)
    arr, count_right = quickSortA(arr, part + 1, right)

    count += count_left + count_right
    return arr, count

def quickSortB(arr, left, right, count = 0):
    arr = list(arr)
    if left >= right - 1:
        return arr, count

    arr[left], arr[right - 1] = arr[right - 1], arr[left]
    count = right - left - 1
    part = partition(arr, left, right)
    arr, count_left = quickSortB(arr, left, part)
    arr, count_right = quickSortB(arr, part + 1, right)

    count += count_left + count_right
    return arr, count

def quickSortC(arr, left, right, count = 0):
    arr = list(arr)
    if left >= right - 1:
        return arr, count

    find_middle = (right - left + 1) / 2 - 1
    median_index = left + find_middle
    first = arr[left]
    last = arr[right - 1]
    middle = arr[median_index]
    three_pivots = [first, last, middle]
    is_middle = []
    is_middle.append(min(three_pivots))
    is_middle.append(max(three_pivots))
    median = set(three_pivots) - set(is_middle)

    if last in median:
        arr[left], arr[right - 1] = arr[right - 1], arr[left]
    elif middle in median:
        arr[left], arr[median_index] = arr[median_index], arr[left]

    count = right - left - 1
    part = partition(arr, left, right)
    arr, count_left = quickSortC(arr, left, part)
    arr, count_right = quickSortC(arr, part + 1, right)

    count += count_left + count_right
    return arr, count

def main():
    # Start time
    start = time()

    # Inicialization
    arr_file = []

    # Open file
    f = open('QuickSort.txt', 'r')
    for line in f: arr_file.append(int(line))
    f.close()

    # Quick Sort type A
    arr_quickSorta, count_a = quickSortA(arr_file, 0, len(arr_file))
    print 'Count comparison qiuck sort case A: %d' % count_a

    # Quick Sort type B
    arr_quickSortb, count_b = quickSortB(arr_file, 0, len(arr_file))
    print 'Count comparison qiuck sort case B: %d' % count_b

    # Quick Sort type C
    arr_quickSortc, count_c = quickSortC(arr_file, 0, len(arr_file))
    print 'Count comparison qiuck sort case C: %d' % count_c

    print 'Elapsed Time: %s' % (time() - start)

if __name__ == '__main__':
    main()