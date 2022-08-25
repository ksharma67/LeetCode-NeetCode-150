class EndSearch(Exception):
    """ exception that ends a search """
	
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: 
        
        def helper(node):
            
            if not node:
                # When we reach a null node, we set that as depth 0
                return 0
            
            l = helper(node.left)
            r = helper(node.right)
            
            if abs(l-r) > 1: # if the difference is more than 1 raise EndSearch
                raise EndSearch
            
            return max(l, r) + 1 # return the maximum depth in this branch and add 1
            
        try:
            helper(root)
            return True
        except EndSearch:
            return False
