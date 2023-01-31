#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = []
        for i in range(0, len(s)):
            a.append(s[i])
        for x in t:
            if x not in a: return False
            #print(x)
            a.remove(x)
            #print(a)
            #print(b)
        if(len(a) != 0): return False
        return True