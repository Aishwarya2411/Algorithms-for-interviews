# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        vals=[]
        decimal =0
        while head:
            decimal=2*decimal+head.val
            head=head.next
        return (decimal)
         
