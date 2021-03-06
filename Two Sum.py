# Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #USING HASHMAPS TC- O(n), SC- O(n)
        dict1={}

        if len(nums)<0:
            return False


        for i in range(len(nums)):
            if nums[i] in dict1:
                return dict1[nums[i]],i

            else:
                dict1[target-nums[i]]=i



#Method- using HASHMAPS
#Iterate throught the array, check if the element is present in the dictionary. If no, store the diff in the dict with i as value for the key. If the element is present then return the i value with the value of the key.
