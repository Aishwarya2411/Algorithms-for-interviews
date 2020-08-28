class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # output=[]
        for i in range (1,n+1):
            
            if i%3==0:
                if i%5==0:
                    yield("FizzBuzz")  #use yield to reduce the space complexity
                else:
                    yield("Fizz")
            elif i%5==0:
                yield("Buzz")
            else:
                yield(str(i))
        # return(output)
