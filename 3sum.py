# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[i]+nums[left]+nums[right]==0:
                    res.append([nums[i],nums[left],nums[right]])
                    left=left+1
                    right=right-1
                elif nums[i]+nums[left]+nums[right]>0:
                    right=right-1
                elif nums[i]+nums[left]+nums[right]<0:
                    left=left+1
        return res

                    
