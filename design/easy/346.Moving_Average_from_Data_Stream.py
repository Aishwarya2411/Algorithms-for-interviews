from collections import deque

class MovingAverage(object):
    
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = deque( maxlen=size)


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        
        return (float (sum(self.q))/float (len(self.q)))
            
