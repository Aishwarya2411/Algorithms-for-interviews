class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        entry={}
        neg=[]
        non_neg=[]
        nums.sort()
        present=set()
        if set(nums)=={0} and len(nums)>=3:
            return ([[0,0, 0]])
        for num in nums:
            entry[num]= entry.setdefault(num,0)+1
            if num<0:
                neg.append(num)
            else:
                non_neg.append(num)
        print (entry)
        for n in neg:
            for p in non_neg:
                if p==0:
                    if entry[p]>=3:
                        present.add((p,p,p))
                value= -n-p
                
                if value in nums:
                    if (value==n) or (value==p):
                        if entry[value]>1:
                            present.add((n, value, p))
                    elif value==0:
                            present.add((n, value, p))
                    elif n<value<p:
                            present.add((n, value, p))

                        
        
       
        return (list (present))
