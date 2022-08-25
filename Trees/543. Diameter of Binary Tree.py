def depth(self, root):
  if not root:
    return 0, 0
  l_diameter, l_depth  = self.depth(root.left)
  r_diameter, r_depth = self.depth(root.right)
  return max(l_depth + r_depth, l_diameter, r_diameter), max(l_depth, r_depth) + 1
    
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
  diameter, depth = self.depth(root)
	# subtracting one from depth as there's no parent node of root node (no edge between parent node and root node).
  return max(diameter, depth-1)
