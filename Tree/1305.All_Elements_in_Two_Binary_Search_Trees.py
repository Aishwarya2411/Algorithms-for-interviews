# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1=[]
        def transverse (root):
            
            if root:
                list1.append(root.val)
                transverse(root.left)
                transverse(root.right)
            return list1
        
        transverse(root1)
        transverse(root2)
        list1.sort()
        return (list1)
        
            
        
