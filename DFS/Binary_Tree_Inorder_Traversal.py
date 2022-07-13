# ОБХОД БИНАРНОГО ДРЕВА

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorderTraversal(self, root):
    res = []

    def dfs(root):
        if root is None:
            return
        dfs(root.left)
        res.append(root.val)
        dfs(root.right)

    dfs(root)

    return res