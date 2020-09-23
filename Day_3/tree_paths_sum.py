#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def tree_paths_sum(root):
    # NOTES:
    # track a sum var
    # do a depth first traversal and add each node to the sum.
    # return sum

    sumOf = 0
    stack = []

    # add the root node to our stack
    stack.append(root)

    # continue popping from our stack so long as there are nodes in it
    while len(stack) > 0:
        current_node = stack.pop()

        # check if this node has children & add tp stack
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

        # calc sum
        sumOf += current_node.value

    return sumOf