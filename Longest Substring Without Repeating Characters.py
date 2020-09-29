# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        di={}
        leng=0
        max_len=0
        start=0
        for i,letter in enumerate(s):
            if letter in di and di[letter]>=start:
                start=di[letter]+1
                leng=i-start+1
                di[letter]=i
            else:
                di[letter]=i
                leng+=1
                max_len=max(max_len,leng)
        return max_len

        #iterate i through the looop and keep track of the length and store the chars whenever there is a distinct char seen.
        #If i finds a char already in hash, update start pointer to the char index+1 and new length as i-startt+1 
