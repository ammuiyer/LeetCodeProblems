#Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = ""
        for i in range(0, len(s)):
            temp = ""
            for j in range(i, len(s)):
                if(s[j] in temp): break
                else:
                    temp = temp + s[j]
            if(len(temp)>len(ans)):
                ans = temp
        return len(ans)
