# ЛИСТ - УЗЕЛ ДЕРЕВА, У КОТОРОГО НЕТУ ПОТОМКОВ (надеюсь верно)

class Node:
    def __init__(self, key):
        self.Key = None
        self.Left = None
        self.Right = None


def num_leaves(items):
    count = 0

    if items.Left is not None:
        count += 1
        count += num_leaves(items.Left)

    if items.Right is not None:
        count += 1
        count += num_leaves(items.Right)

    return count


