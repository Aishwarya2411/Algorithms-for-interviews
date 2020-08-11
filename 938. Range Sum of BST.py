# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        node_val=[]
        
        def printPreorder(root): 
          
  
          if root: 
  
             
             node_val.append(root.val)
             printPreorder(root.left) 
  
             printPreorder(root.right) 
          
        
        printPreorder (root)
        sum_nodes=0
        for i in node_val:
            if L<=i<=R:
                sum_nodes+=i
        return(sum_nodes)
                
