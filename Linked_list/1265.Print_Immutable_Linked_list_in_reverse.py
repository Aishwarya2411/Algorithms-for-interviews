class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        
        if (head.getNext()!=None):
            self.printLinkedListInReverse(head.getNext())
            head.printValue()
        else:
            head.printValue()

            
