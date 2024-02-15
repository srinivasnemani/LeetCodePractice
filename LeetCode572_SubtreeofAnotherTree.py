# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot:  # Null tree is always a subtree
            return True
        if not root:  # Non-null tree cannot be a subtree of a null tree
            return False
        # Check if trees are identical or if subRoot is a subtree of either branch
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,
                                                                                                      subRoot)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Check if both trees are empty
        if not p and not q:
            return True
        # One tree is empty, the other is not
        if not p or not q:
            return False
        # The values at the nodes are different
        if p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
