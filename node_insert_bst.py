__author__ = 'raiahn'

from Node import Node
from init_graph import init_graph
from in_order import in_order


def insert_node(root, value):

    if root is None:
        root = Node(value)

    else:
        while root.right is not None:
            if value > root.value:
                root = root.right
            else:
                root = root.left
        if root.left is None:
            root.left = Node(value)
        else:
            root.right = Node(value)
    return root


rt = init_graph()
in_order(rt)
print("\n")
rt1 = insert_node(rt, 13)
in_order(rt)




