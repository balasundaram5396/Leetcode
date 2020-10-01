# Share
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return [""]

        if len(strs)==1:
            return [strs]

        a={}

        for s in strs:
            sorted_s="".join(sorted(s))

            if sorted_s not in a:
                a[sorted_s]=[s]
            else:
                a[sorted_s].append(s)

        res=[]

        for item in a.values():
            res.append(item)

        return res



#traverse through the array of strs, sort each item and check kif it is in the dict,
#if no then add it with the item as value else append the item to the value array for that key.        
