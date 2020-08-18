
import collections
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        self.words= words
        self.chars=chars
      
        
        good =[]
    
        words = [str(x) for x in words]
        chars = [str(x) for x in chars]
        
        chars_frequency = collections.Counter(chars)
       
        for word in words:
            unique = all(letter in chars for letter in word)
            word_freq = collections.Counter(word)
            if unique:
                word_len =0
                for i in word:
                    if chars_frequency[i]>=word_freq[i]:
                        word_len +=1
                if word_len==len(word):
                        good.append(word)
        print (good)
        ans = 0
        for i in good:
            ans+=len(i)
        return (ans)
