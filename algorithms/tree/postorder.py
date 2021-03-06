'''
Time complexity : O(n)
'''

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder(root):
    res_temp = []
    res = []
    if not root:
        return res
    stack = []
    stack.append(root)
    while stack:
        root = stack.pop()
        res_temp.append(root.val)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
    while res_temp:
        res.append(res_temp.pop())
    return res

# Recursive Implementation
def postorder_rec(root, res=None):
    if root is None:
        return []
    if res is None:
        res = []
    postorder_rec(root.left, res)
    postorder_rec(root.right, res)
    res.append(root.val)
    return res



if __name__ == '__main__':
    n1 = Node(100)
    n2 = Node(50)
    n3 = Node(150)
    n4 = Node(25)
    n5 = Node(75)
    n6 = Node(125)
    n7 = Node(175)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7

    assert postorder(n1)     == [25, 75, 50, 125, 175, 150, 100]
    assert postorder_rec(n1) == [25, 75, 50, 125, 175, 150, 100]
