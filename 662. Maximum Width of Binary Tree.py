# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
       
        Q=[[root,0]]
        if root!= None:
            res=1
            while len(Q)>0:
                
                count = len(Q)
                leftmost=Q[0][1]
                rightmost=Q[-1][1]
                res= max(res, rightmost-leftmost+1)
                for i in range (count):
                    pos =Q[0]
                    index=pos[1]-leftmost
                    Q.pop(0)
                    if pos[0].left!=None:
                        Q.append([pos[0].left,2*index+1])
                    if pos[0].right!=None:
                        Q.append([pos[0].right,2*index+2])
            return res
        else:
            return 0
        
                        
