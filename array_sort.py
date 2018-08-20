from utils import log


def insertion(array):
    a = array
    length = len(array)
    j = 1
    while j < length:
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
        j += 1


def selection(array):
    a = array
    length = len(a)
    i = 0
    while i < length:
        j = i + 1
        min = i
        while j < length:
            if a[j] < a[min]:
                min = j
            j += 1
        a[i], a[min] = a[min], a[i]
        i += 1


def bubble(array):
    a = array
    length = len(a) - 1
    max = length
    while max > 0:
        i = 0
        while i < length:
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
            i += 1
        max -= 1


def heap_parent(index):
    return (index + 1) // 2


def heap_left(index):
    i = 2 * (index + 1) - 1
    return i


def heap_right(index):
    return heap_left(index) + 1


def heap_max_heapify(array, index, heap_size):
    a = array
    size = heap_size
    i = index
    if i < size:
        l = heap_left(i)
        r = heap_right(i)
    else:
        return
    if l < size and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r < size and a[r] > a[largest]:
        largest = r
    if not (largest == i):
        a[i], a[largest] = a[largest], a[i]
        heap_max_heapify(a, largest, size)


def heap_build_max_heap(array):
    a = array
    size = len(a)
    length = size // 2
    for i in range(length - 1, -1, -1):
        heap_max_heapify(a, i, size)


def heap(array):
    a = array
    heap_build_max_heap(a)
    size = len(a)
    length = size - 1
    i = size - 1
    for i in range(length, 0, -1):
        a[i], a[0] = a[0], a[i]
        size -= 1
        heap_max_heapify(a, 0, size)


def quick_partition(array, start, end):
    a = array
    p = start
    r = end
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[r] = a[r], a[i]
    return i


def quick_recursion(array, start, end):
    a = array
    p = start
    r = end
    if p < r:
        q = quick_partition(a, p, r)
        quick_recursion(a, p, q - 1)
        quick_recursion(a, q + 1, r)


def quick(array):
    length = len(array) - 1
    quick_recursion(array, 0, length)
