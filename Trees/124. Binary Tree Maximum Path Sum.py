# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = root.val
        
        def helper(root):
            if not root:
                return 0
            
            l = helper(root.left)
            r = helper(root.right)
            
            self.best = max(self.best, root.val, root.val + l, root.val + r, root.val + l + r)
            
            return max(root.val, root.val + l, root.val + r)
        
        helper(root)
        return self.best
