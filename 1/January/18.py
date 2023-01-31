#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = self.strip(s)
        for i in range(0, (len(s)/2)):
            if(s[i]!=s[len(s)-i-1]):
                return False
        return True
    def strip(self, s):
        ans = s.lower()
        ans2 = ""
        for i in range(0, len(ans)):
            if((ord(ans[i])>=65) and (ord(ans[i])<=122)):
                ans2 = ans2 + ans[i]
        return ans2

 

