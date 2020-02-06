# [3Grid Unique Paths](https://www.interviewbit.com/problems/grid-unique-paths/)

## solution (Owen) 

```python
import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        n=A-1+B-1
        m=A-1
        return self.helper(n,m)
    def helper(self,n,m):
        return math.factorial(n)/(math.factorial(n-m)*math.factorial(m))
```
### takeaway 

- just a math quiz 
- another way is f(x,y)=f(x-1,y)+f(x,y-1)
