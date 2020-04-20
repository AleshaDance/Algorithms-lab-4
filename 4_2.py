class Tree(object):
    def __init__(self):
        self.Key = None
        self.Left = None
        self.Right = None


def balanced(items):
    if len(items) != 0:
        step = Tree()
        step.Left = balanced(items[:len(items) // 2])
        step.Right = balanced(items[len(items) // 2 + 1:])
        step.Key = items[len(items) // 2]
        return step
    else:
        return None


def show(base):
    if base != None:
        print('\t  {}'.format(base.Key))
        print('\t/    \\')
        print('{}    {}'.format(balanced(base.Left), balanced(base.Right)))


if __name__ == "__main__":
    with open("tree_data.txt") as file:
        tree_data = [x for x in file.readline().split(" ")]
    base = balanced(tree_data)
    show(base)








