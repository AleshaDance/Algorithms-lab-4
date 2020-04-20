class Tree:
    def __init__(self, key):
        self.Key = key
        self.Left = None
        self.Right = None


# ЧТЕНИЕ ВЫРАЖЕНИЯ С ДЕРЕВА
def read_from_tree(t):
    if t is not None:
        if t.Left != None:
            print("(", end='')
        read_from_tree(t.Left)
        print(t.Key, end='')
        read_from_tree(t.Right)
        if t.Left != None:
            print(")", end='')


# РЕШЕНИЕ
def solve(t):
    if t.Key == "+":
        return solve(t.Left) + solve(t.Right)
    elif t.Key == "-":
        return solve(t.Left) - solve(t.Right)
    elif t.Key == "*":
        return solve(t.Left) * solve(t.Right)
    elif t.Key == "/":
        return solve(t.Left) // solve(t.Right)
    else:
        return int(t.Key)


# ПОСТРОЕНИЕ ДЕРЕВА
def BuildTree(input):
    items = []
    for item in input:
        if not (item == '+' or item == '-' or item == '*' or item == '/'):
            t = Tree(item)
            items.append(t)
        else:
            new_node = Tree(item)
            new_node.Right = items.pop()
            new_node.Left = items.pop()
            items.append(new_node)
    t = items.pop()
    return t


if __name__ == "__main__":
    string = "76 12 80 + * 12 +"
    tree = BuildTree(string.split(' '))
    read_from_tree(tree)
    print(" = {}".format(solve(tree)))
