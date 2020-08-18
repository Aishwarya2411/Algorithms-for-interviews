class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if name ==typed:
            return True
        
        i,j=0,0
        typed_unique= ''.join(OrderedDict.fromkeys(typed).keys())
        name_unique= ''.join(OrderedDict.fromkeys(name).keys())
        
        while i<len(name) and j<len(typed):
           
            if name[i]==typed[j]:
                
                i+=1
                j+=1
            elif typed[j]==typed[j-1]:
                
                j+=1
            else:
                return False
       
        if i==len(name) and typed_unique==name_unique:
            return True
        
