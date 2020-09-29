# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.


class Solution:
    def majorityElement(self, num):
        #nums.sort()
        #return nums[len(nums)//2]

        a={}
        for num in nums:
            if num not in a:
               a[num]=1
           if a[num]>(len(nums)//2):
               return num
           else:
               a[num]+=1
           
