class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        
        ##two pointer##
        
            last_index={c:i for i, c in enumerate (S)}
            end= 0
            start=0
            output=[]
            for i, char in enumerate (S):
                
                end = max(end, last_index[char])
            
                if end==i:
                    output.append(end-start+1)
                    start=end+1
                
            return output
