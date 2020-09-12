class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1= version1.split(".")
        version2= version2.split(".")
        max_len= max(len(version1),len (version2))
        
        for i in range(max_len):
            if i< len(version1):
                i1= int(version1[i])
                
            else:
                i1=0
            if i< len(version2):
                i2= int(version2[i])
               
            else:
                i2=0
            if i1!=i2:
                if i1>i2:
                    return 1
                else:
                    return -1
        return 0
