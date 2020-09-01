# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        for i in range(1,len(nums)):
            if nums[l]!=nums[i]:
                l+=1
                nums[l]=nums[i]
        return l+1        
                
        
#TC- O(n)
#SC- O(1)                