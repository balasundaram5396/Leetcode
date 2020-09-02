# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #APPROACH 1 TC- O(n), SC- O(n)
#         inp={}
#         for num in nums:
#             if num in inp:
#                 inp[num]+=1
                
#             else:
#                 inp[num]=1
#             if inp[num]>1:
#                 return True
            
            #APPROACH 2 TC- O(n), SC- O(1)
            if len(nums)-len(set(nums)):
                return True
            else:
                return False
            