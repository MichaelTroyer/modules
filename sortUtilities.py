# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:01:56 2017

@author: michael
"""


import random


def shuffle_data():
    random.seed(4)
    return random.shuffle(DATA)


def selection_sort(data):
    for scanIndex in range(0, len(data)):
        minIndex = scanIndex

        for compIndex in range(scanIndex + 1, len(data)):
            if data[compIndex] < data[minIndex]:
                minIndex = compIndex

        if minIndex != scanIndex:
            data[scanIndex], data[minIndex] = data[minIndex], data[scanIndex]
            print(data)


def insertion_sort(data):
    for scanIndex in range(1, len(data)):
        temp = data[scanIndex]

        minIndex = scanIndex

        while minIndex > 0 and temp < data[minIndex - 1]:
            data[minIndex] = data[minIndex - 1]
            minIndex -= 1

        data[minIndex] = temp
        print(data)


def merge_sort(data):
    # Determine whether the list is broken into individual pieces.
    if len(data) < 2:
        return data

    # Find the middle of the list.
    middle = len(data)//2

    # Break the list into two pieces.
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    # Merge the two sorted pieces into a larger piece.
    print("Left side: ", left)
    print("Right side: ", right)
    merged = merge(left, right)
    print("Merged ", merged)
    return merged


def merge(left, right):
    # When the left side or the right side is empty, it means that this is an
    # individual item and is already sorted.
    if not len(left):
        return left
    if not len(right):
        return right

    # Define variables used to merge the two pieces.
    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)

    # Keep working until all of the items are merged.
    while (len(result) < totalLen):

        # Perform the comparisons and merge the pieces according to value.
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

        # When the left side or the right side is longer, add the remaining
        # elements to the result.
        if leftIndex == len(left) or rightIndex == len(right):
            result.extend(left[leftIndex:] or right[rightIndex:])
            break
    return result


def quick_sort(data, left, right):
    if right <= left:
        return None
    else:
        pivot = partition(data, left, right)
        quick_sort(data, left, pivot-1)
        quick_sort(data, pivot+1, right)
    return data


def partition(data, left, right):
    print('Partitioning - {}'.format(data[left:right + 1]))

    pivot = data[left]
    lIndex = left + 1
    rIndex = right

    print('Pivot: {}'.format(pivot))

    while True:
        print('lIndex = {}: {}'.format(lIndex, data[lIndex]))
        print('rIndex = {}: {}'.format(rIndex, data[rIndex]))

        while lIndex <= rIndex and data[lIndex] <= pivot:
            lIndex += 1
            print('lIndex -> {}: {}'.format(lIndex, data[lIndex]))

        while rIndex >= lIndex and data[rIndex] >= pivot:
            rIndex -= 1
            print('rIndex -> {}: {}'.format(rIndex, data[rIndex]))

        if rIndex <= lIndex:
            print('Index collision - {}: {}'.format(rIndex, data[rIndex]))
            break

        print('Switching: {} and {}'.format(data[lIndex], data[rIndex]))
        data[lIndex], data[rIndex] = data[rIndex], data[lIndex]
        print(data[left:right + 1])

    print('Switching with pivot: {} - {}'.format(data[left], data[rIndex]))
    data[left], data[rIndex] = data[rIndex], data[left]
    print(data[left:right + 1])
    print('Pivot - {}: {}'.format(rIndex, data[rIndex]))
    return rIndex


if __name__ == '__main__':

    import timeit

    DATA = [8, 9, 7, 10, 3, 1, 4, 6, 2, 5, 5, 5, 6, 2, 9, 0]

    def wrapper(func, *args, **kwargs):
        def wrapped():
            return func(*args, **kwargs)
        return wrapped

    selection = wrapper(selection_sort, data=DATA)

    print selection_sort(DATA)
    shuffle_data()
    print
    print insertion_sort(DATA)
    shuffle_data()
    print
    print merge_sort(DATA)
    shuffle_data()
    print
    print quick_sort(DATA, 0, len(DATA) - 1)
    shuffle_data()
