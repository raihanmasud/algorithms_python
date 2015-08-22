__author__ = 'raihan'

from init_graph import init_graph


def in_order(root):
    if root is None:
        return False
    else:
        in_order(root.left)
        print(root.value)
        in_order(root.right)

#test inorder
#rt = init_graph()
#in_order(rt)