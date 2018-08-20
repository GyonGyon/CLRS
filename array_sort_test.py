# import random
from array_sort import insertion, selection, bubble, heap, quick
from utils import log, random_array
import time
import enum
from utils import log


class Config(enum.IntEnum):
    loop_count = 1000
    test_array_length = 100


def template(func, name, size):
    a = random_array(size)
    aback = list(a)
    expected = sorted(a)
    t1 = time.time()
    func(a)
    t2 = time.time()
    if str(expected) == str(a):
        t = t2 - t1
        return (True, t)
    else:
        s = 'failed: {}\nbefore: ({})\nafter : ({})'.format(name, aback, a)
        print(s)
        return (False, 0)


def loop_t(func, name, count=Config.loop_count, size=Config.test_array_length):
    time = 0
    for i in range(count):
        i
        (success, t) = template(func, name, size)
        if not success:
            return
        else:
            time += t
    print('成功: {}, 时间: {}, 次数: {}, 长度: {}'.format(name, time, count, size))


# def random_array(size=8):
#     a = list(range(size))
#     # shuffle works in place and returns None
#     random.shuffle(a)
#     return a


# def test_bubble():
#     lq = random_array()
#     lr = list(lq)
#     lr.sort()
#     bubble(lq)
#     try:
#         assert lq == lr
#     except:
#         log(lq, lr)


# def test_insertion():
#     lq = random_array()
#     lr = list(lq)
#     lr.sort()
#     insertion(lq)
#     try:
#         assert lq == lr
#     except:
#         log(lq, lr)


# def test_selection():
#     lq = random_array()
#     lr = list(lq)
#     lr.sort()
#     selection(lq)
#     try:
#         assert lq == lr
#     except:
#         log(lq, lr)


# def test_heap_max_heapify():
#     a = random_array()
#     heap(a)


# def test_log_heap():
#     a=random_array(10)
#     # utils.log_heap(a)


# def test_heap():
#     lq=random_array()
#     # loop_t(heap, 'heap')


# def test_quick():
#     lq=random_array()
#     # loop_t(quick, 'quick')

def contrast():
    loop_t(bubble, 'bubble')
    loop_t(insertion, 'insertion')
    loop_t(selection, 'selection')
    loop_t(heap, 'heap')
    loop_t(quick, 'quick')

def test_contrast():
    contrast()
    pass


def run_all():
    test_bubble()
    test_heap()
    test_insertion()
    test_quick()
    test_selection()


if __name__ == '__main__':
    # run_all()
    contrast()
