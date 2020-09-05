
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        count=[1]*len(arr)
        for i in range (0,len(arr)):
           
            if arr[i+1-m:i+1]== arr[i+1-2*m:i+1-m]:
                count[i]=1+count[i-m]

                if count[i]==k:
                    return True
        return False
