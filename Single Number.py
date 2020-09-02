# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #using Hashmaps TC- O(n) & SC- O(n)
#         a={}
#         for num in nums:
#             if num in a:
#                 a[num]+=1
#             else:
#                 a[num]=1
#         for i in a:
#             if a[i]==1:
#                 return i
        
    
        #Using XOR operator TC- O(n) & SC- O(1)
        num=0
        for i in nums:
            num^=i
        return num