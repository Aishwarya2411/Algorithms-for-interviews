class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
       
        ans_dict={}
        nums.sort()
        present =set ()
        # if len(nums)<3:
        #     return ([])
        if set(nums)=={0} and len(nums)>3:
            return ([[0,0, 0]])
        else:
            for i, target in enumerate (nums):

                hashmap={}
                for j, element in enumerate (nums[i+1:]):
                    sub= -(target+element)

                    if sub in hashmap and sub in nums:
                            min_val = min(target,sub,element)
                            max_val = max (target,sub,element)
                            if (min_val, max_val) not in present:
                                present.add((min_val,max_val))
                                ans_dict[len(ans_dict)+1]=[target,sub,element]

                    hashmap[element]=j
           
            return (ans_dict.values())
