# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        ans =float('inf')
        while (root):
            close=int (round(target))
            if abs(target - ans) > abs(target - root.val):
                 ans=root.val
               
            elif root.val<close:
                 
                 root= root.right
            else:
                root=root.left
        return ans
