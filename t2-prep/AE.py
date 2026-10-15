from sys import stdin as sd

sd.setrecursionlimit(1 << 20)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(inorder, postorder):
    if not inorder:
        return None

    root_v = postorder[-1]
    root = Node(root_v)

    idx = inorder.index(root_v)

    root.left = build_tree(inorder[:idx], postorder[:idx])
    root.right = build_tree(inorder[idx + 1:], postorder[idx:-1])

    return root


min_sum = float("inf")
best_leaf = float("inf")


def check_path(node, curr_sum):
    global min_sum, best_leaf

    if node is None:
        return

    curr_sum += node.val

    if node.left is None and node.right is None:
        if curr_sum < min_sum:
            min_sum = curr_sum
            best_leaf = node.val
        elif curr_sum == min_sum and node.val < best_leaf:
            best_leaf = node.val
        return

    check_path(node.left, curr_sum)
    check_path(node.right, curr_sum)


def main(sd):
    global min_sum, best_leaf

    lines = sd.read().splitlines()
    i = 0

    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue

        inorder = list(map(int, lines[i].split()))
        postorder = list(map(int, lines[i + 1].split()))
        i += 2  

        min_sum = float("inf")
        best_leaf = float("inf")

        tree = build_tree(inorder, postorder)
        check_path(tree, 0)
        print(best_leaf)

main(sd)