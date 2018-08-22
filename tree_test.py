from tree import *


def create_tree_breadth(array):
    size = len(array)
    if size <= 0:
        return None
    root = TreeNode(array[0])
    i = 1
    tmps = [root]
    while i < size:
        tmps2 = []
        for tmp in tmps:
            if i < size:
                v = array[i]
                tmp.left = TreeNode(v)
                tmps2.append(tmp.left)
                i += 1
            if i < size:
                v = array[i]
                tmp.right = TreeNode(v)
                tmps2.append(tmp.right)
                i += 1
        tmps = tmps2
    return root


def test_pre_order_recur():
    args = [
        [range(0), []],
        [range(1), [0]],
        [range(4), [0, 1, 3, 2]],
        [range(10), [0, 1, 3, 7, 8, 4, 9, 2, 5, 6]],
    ]
    for arg in args:
        l = list(arg[0])
        ans = arg[1]
        root = create_tree_breadth(l)
        que = []

        def callback(tree):
            que.append(tree.value)
        pre_order_recur(root, callback)
        assert que == ans


def test_in_order_recur():
    args = [
        [range(0), []],
        [range(1), [0]],
        [range(4), [3, 1, 0, 2]],
        [range(10), [7, 3, 8, 1, 9, 4, 0, 5, 2, 6]],
    ]
    for arg in args:
        l = list(arg[0])
        ans = arg[1]
        root = create_tree_breadth(l)
        que = []

        def callback(tree):
            que.append(tree.value)
        in_order_recur(root, callback)
        assert que == ans


def test_post_order_recur():
    args = [
        [range(0), []],
        [range(1), [0]],
        [range(4), [3, 1, 2, 0]],
        [range(10), [7, 8, 3, 9, 4, 1, 5, 6, 2, 0]],
    ]
    for arg in args:
        l = list(arg[0])
        ans = arg[1]
        root = create_tree_breadth(l)
        que = []

        def callback(tree):
            que.append(tree.value)
        post_order_recur(root, callback)
        assert que == ans


def main():
    test_pre_order_recur()
    test_in_order_recur()
    test_post_order_recur()


main()
