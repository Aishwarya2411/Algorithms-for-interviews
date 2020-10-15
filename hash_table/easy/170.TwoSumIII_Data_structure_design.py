class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num =[]

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        
        self.num.append (number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        hashmap={}
        
        for i in range (len(self.num)):
            target= value- self.num[i]
            index=i
            if target in hashmap and hashmap[target]!= index:
                return True
            hashmap[self.num[i]]=index
        return False
            


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
