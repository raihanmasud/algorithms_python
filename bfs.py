__author__ = 'raihan'

from Queue import Queue
import init_graph


def bfs(root, item):

    if root is None:
        return False

    else:
        queue = Queue()
        queue.enqueue(root)

    while not queue.is_empty():

        root = queue.peek()
        print(root.value)
        if root.value == item:
            return True
        queue.deque()

        if root.left is not None:
            queue.enqueue(root.left)

        if root.right is not None:
            queue.enqueue(root.right)


rt = init_graph()
bfs(rt, 0)
