# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        APPROCH 1
        use two variables, temp1: 1,2,3,4,5 (reject6 and 7) and temp2: 1,2,3,4,5,6(reject 7)
        1,2,3 in temp2--> choose temp1
        4,5,6 in temp2--> choose temp1+5
        """
       
        temp1, temp2= rand7(), rand7()
        while temp1>5: temp1=rand7()
        while temp2==7: temp2= rand7()
        
        if 1<=temp2<=3:
            return(temp1)
        elif 4<=temp2<=6:
            return (temp1+5)
        
        """To optimize this use rejection sampling method - temp=(7*(rand7()-1)) + (rand7()-1), this ll give you sets od [0,9], [10,19],[20,29],[30, 39], [40,48], all sets are equal except the last one so reject if the temp value>=40 and return temp1%10-1"""
        
        ##APPROCH 2
        
        val=(7*(rand7()-1)) + (rand7()-1)
        while val>=40:val=(7*(rand7()-1)) + (rand7()-1)
        return ((val%10)+1)
        
