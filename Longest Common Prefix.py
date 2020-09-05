# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        minLen=len(strs[0])
        for i in range(len(strs)):
            minLen=min(minLen,len(strs[i]))
        res=""
        i=0
        while i <minLen:
            first=strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i]!=first:
                    return res
            res=res+first
            i=i+1
        return res
        