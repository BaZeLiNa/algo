class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


total_sum = 0


def left_child_sum(func_root):
    global total_sum
    if func_root is None:
        return 0

    if func_root.left is not None and func_root.left.left is None and func_root.left.right is None:
        total_sum += func_root.left.value

    left_child_sum(func_root.left)
    left_child_sum(func_root.right)
    return total_sum


if __name__ == "__main__":
    root = BinaryTree(3)
    root.left = BinaryTree(9)
    root.right = BinaryTree(20)
    root.right.left = BinaryTree(15)
    root.right.right = BinaryTree(7)

    print(left_child_sum(root))
