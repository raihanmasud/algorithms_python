__author__ = 'raihan'
# recursive dfs

from init_graph import init_graph


def dfs(root, item):
    if root is None:
        return False
    else:
        print(root.value)
        if root.value == item:
            return True
        dfs(root.left, item)
        dfs(root.right, item)


rt = init_graph()
dfs(rt, 0)

#dfs(None, 2)
