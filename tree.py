class TreeNode:
    def __init__(self, n):
        self.value = n
        self.left = None
        self.right = None


def pre_order_recur(node, callback):
    if node == None:
        return
    callback(node)
    if node.left != None:
        pre_order_recur(node.left, callback)
    if node.right != None:
        pre_order_recur(node.right, callback)


def in_order_recur(node, callback):
    if node == None:
        return
    if node.left != None:
        in_order_recur(node.left, callback)
    callback(node)
    if node.right != None:
        in_order_recur(node.right, callback)


def post_order_recur(node, callback):
    if node == None:
        return
    if node.left != None:
        post_order_recur(node.left, callback)
    if node.right != None:
        post_order_recur(node.right, callback)
    callback(node)
