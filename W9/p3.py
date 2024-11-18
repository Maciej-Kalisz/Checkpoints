class TreeNode:
    def __init__(self, payload, left, right):
        self.payload = payload
        self.left = left
        self.right = right

    def get_payload(self):
        return self.payload

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

def build_tree():
    leaf1 = TreeNode("Leaf 1", None, None)
    leaf2 = TreeNode("Leaf 2", None, None)
    leaf3 = TreeNode("Leaf 3", None, None)
    leaf4 = TreeNode("Leaf 4", None, None)

    internal1 = TreeNode("Internal 1", leaf1, leaf2)
    internal2 = TreeNode("Internal 2", leaf3, leaf4)

    root = TreeNode("Root", internal1, internal2)

    return root

def print_left(tree_node):
    if not type(tree_node) is TreeNode:
        return None

    cur = tree_node

    while not cur.get_left() is None:
        print(cur.get_payload())
        cur = cur.get_left()

    print(cur.get_payload())

def print_right(tree_node):
    if not type(tree_node) is TreeNode:
        return None

    cur = tree_node

    while not cur.get_right() is None:
        print(cur.get_payload())
        cur = cur.get_right()

    print(cur.get_payload())