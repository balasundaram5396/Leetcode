# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s=list(s)
        a={}
        for i in range(len(s)):
            if s[i] in a:
                a[s[i]]+=1
            else:
                a[s[i]]=1
        for i in range(len(s)):
            if a[s[i]]==1:
                return i
        return -1
            
    #TC- O(n), SC -(1)