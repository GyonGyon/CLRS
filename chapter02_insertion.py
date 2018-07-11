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
