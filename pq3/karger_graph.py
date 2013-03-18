# coding: utf-8

from time import time
from random import randint
import copy

def randomNode(arr):
    node1 = arr.keys()[randint(0, len(arr) - 1)]
    node2 = arr[node1][randint(0, len(arr[node1]) - 1)]

    return node1, node2

def kargerMinCut(arr):
    arr_cp = copy.deepcopy(arr)
    while len(arr_cp) > 2:
        node1, node2 = randomNode(arr_cp)
        arr_cp[node1] += arr_cp[node2]

        for x in arr_cp[node2]:
            exmpl = arr_cp[x]
            for i in range(0, len(exmpl)):
                if exmpl[i] == node2:
                    exmpl[i] = node1

        while node1 in arr_cp[node1]:
            arr_cp[node1].remove(node1)

        del arr_cp[node2]
    return len(arr_cp[arr_cp.keys()[0]])

def main():
    # Start time
    start = time()

    # Inicialization
    arr_file = {}

    # Open file
    f = open('kargerAdj.txt', 'r')
    for line in f:
        line = line.split()
        arr_file[int(line[0])] = [int(x) for x in line[1:]]
    f.close()

    # Algorinm
    min_cut = kargerMinCut(arr_file)
    for i in range(0, 1000):
        pretender = kargerMinCut(arr_file)
        if pretender < min_cut:
            min_cut = pretender

    print 'Minimum Cuts of graph Karger algorithm: %d' % min_cut
    print 'Elapsed Time: %s' % (time() - start)

if __name__ == '__main__':
    main()