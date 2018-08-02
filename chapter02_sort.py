# from utils import log


def merge(array, start, middle, end):
    p = start
    q = middle
    r = end
    n1 = q - p + 1
    n2 = r - q
    a1 = array[p, q]
    a1.push(float())
    a2 = array[q+1, r]


def merge_sort(array, start, end):
    a = array
    p = start
    r = end
    if p < r:
        q = [(p + r) / 2]
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)


# TODO:
