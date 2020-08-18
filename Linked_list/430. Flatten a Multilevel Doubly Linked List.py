"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.child = None
        
        

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        new_node= Node (head)
        node=head
      
        
        while node!=None:
         
            if node.child:
                
                
                temp=node.child
                while temp.next:
                    temp=temp.next
                temp.next=node.next
                
                if node.next!=None:
                    node.next.prev=temp
                
                node.next=node.child
                
                node.child.prev=node
                node.child=None
                
            node= node.next
            
        
         
        
        return (new_node.val)
            
