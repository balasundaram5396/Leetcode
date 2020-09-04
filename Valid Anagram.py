# Given two strings s and t , write a function to determine if t is an anagram of s.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
        
        #TC- O(n), SC- (1)