__author__ = 'raihan'
# recursive dfs

from Stack import Stack
from init_graph import init_graph


def dfs_stack(root, item):
    if root is None:
        return False
    else:
        stack = Stack()

        stack.push(root)
        while not stack.is_empty():

            print(stack.peek().value)
            root = stack.peek()
            stack.pop()

            if root.value == item:
                return True

            if root.right is not None:
                stack.push(root.right)
                #root = root.right

            if root.left is not None:
                stack.push(root.left)
                #root = root.left


rt = init_graph()
dfs_stack(rt, 0)
# dfs(None, 2)
