class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        after_split= s.split(" ")
        
        after_split=[x for x in after_split if x!=""]
        if len(after_split)==0:
            return 0
        last_word= after_split[-1]
        return (len(last_word))
