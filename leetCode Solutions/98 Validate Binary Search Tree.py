# url : https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validation(root, float("-inf"), float("+inf"))

    def validation(self, root, minVal, maxVal):
        if root is None:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        validateLeft = self.validation(root.left, minVal, root.val)
        validateRight = self.validation(root.right, root.val, maxVal)
        return validateLeft and validateRight
