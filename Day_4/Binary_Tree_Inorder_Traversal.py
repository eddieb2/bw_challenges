# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # ------------------------------------ #
        #         SOLUTION 1: Recursion        #
        # ------------------------------------ #

                # order = []
                # node = root
                #
                # def helper_fxn(node):
                #     if node != None:
                #         if node.left:
                #             helper_fxn(node.left)
                #
                #         order.append(node.val)
                #
                #         if node.right:
                #             helper_fxn(node.right)
                #
                # helper_fxn(node)
                # return order

        # ------------------------------------ #
        #         SOLUTION 2: Iterative        #
        # ------------------------------------ #
        # create empty stack
        # initialize cur node as root
        # push the current node to stack and set cur = cur.left until cur is None
        # if cur is Null and stack is not empty then
        # pop the top item from stack
        # print the popped item set cur = popped item.right
        # step 3
        # if cur is null and stack is empty break

        stack = []
        order = []
        cur = root

        while True:
            while cur != None:
                stack.append(cur)
                cur = cur.left

            if cur == None and len(stack) > 0:
                popped = stack.pop()
                order.append(popped.val)
                cur = popped.right

            if cur == None and len(stack) == 0:
                return order

