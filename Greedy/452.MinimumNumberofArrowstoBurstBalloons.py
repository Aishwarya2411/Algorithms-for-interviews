class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)==0:
            return 0
        points.sort(key=lambda x:x[1])
        arrow=1
        end_point= points[0][1]
  
        for point in points:
           
            if point[0]> end_point:
                arrow+=1
                end_point= point[1]
        return (arrow)
        
