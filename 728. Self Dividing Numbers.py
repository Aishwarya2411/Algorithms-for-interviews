class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def self_div (num,temp):
            digits=[]
            while num >0:
                digits.append(num%10)
                num=num/10
           
            divide=[]
            if all(digits)!=0:
                for i in digits:
                
                    if temp%i==0:
                        divide.append(digits)
                if len(digits)==len(divide):
                    return True
                else:
                    return False
            else:
                return False
            
        self_div_num=[]
        for i in range (left,right+1,1):
         
            # self_div(i,i)
            if self_div (i,i) is True:
              
                self_div_num.append(i)
        return(self_div_num)
