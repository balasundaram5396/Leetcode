# Given a 32-bit signed integer, reverse digits of an integer.

class Solution:
    def reverse(self, x: int) -> int:
        res=0
        if x<0:
            x=abs(x)
            while(x!=0): 
                a=x%10
                res=res*10+a
                x=x//10
            res=-1*res
        else:
            while(x!=0): 
                a=x%10
                res=res*10+a
                x=x//10
        if abs(res) < 2147483648:
                return res
        else:
                return 0

        #TC- O(n), SC- O(1)