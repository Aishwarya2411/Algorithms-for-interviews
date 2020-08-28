class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def binary_search (intervals, left, right, search):
            
            if right>= left:
                if intervals[left][0]>= search:
                   
                    return (intervals[left])
                mid = left+ (right-left)//2

                if intervals[mid][0]< search:
                    return (binary_search(intervals, mid+1, right, search))
                else:
                    return (binary_search(intervals, left, mid, search))
            else:
                return(-1)
        
                
        output=[0]*len(intervals)        
        hashmap={}           # hashmap to keep track of the original index
        
        for i in range (len(intervals)):
            hashmap[tuple(intervals[i])]= i
            
            
        intervals.sort(key=lambda interval:interval[0])  # sort the list so the next interval is higher than the previous one
        
        for i in range (len(intervals)):
               
               val= binary_search(intervals, i, len(intervals)-1, intervals[i][1])
               
               if val!=-1:
                  temp=hashmap.get((val[0], val[1]))
                  output[hashmap.get((intervals[i][0],intervals[i][1]))]= temp
               else:
                output[hashmap.get((intervals[i][0],intervals[i][1]))]=val
        return (output)
    
    
    """Tried brute force first, got TLE for a huge input
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        output=[0]*len(intervals)
        
        for i in range (len(intervals)):
            minval= float("inf")
            right=-1
            for j in range (len(intervals)):
                if intervals[j][0]>=intervals[i][1] and intervals[j][0]<minval:
                    minval= intervals[j][0]
                    right= j
            output[i]= right
           
        return(output)  """
            
