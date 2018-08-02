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
