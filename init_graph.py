__author__ = 'raihan'

from Node import Node


def init_graph():
    four = Node(4, None, None)
    #one = Node(1, None, None)
    eight = Node(8, None, None)
    five = Node(5, four, eight)
    eleven = Node(11, None, None)
    twelve = Node(12, eleven, None)
    root = Node(10, five, twelve)
    return root

