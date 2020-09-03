# 
class Solution:
    def moveZeroes(self, num: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start,end=0,1
        while end<len(num):
            if num[start]==0 and num[end]==0:
                end+=1
            elif num[start]==0 and num[end]!=0:
                num[start],num[end]=num[end],num[start]
                start+=1
                end+=1
            else:
                start+=1
                end+=1
        return num
       
       #TC- O(n), SC- O(1)