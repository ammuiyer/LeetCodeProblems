# 9. Palindrome Number
#Given an integer x, return true if x is a 
#palindrome
# and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        for i in range (0, len(x)):
            j = len(x)-1-i
            if(x[i]!=x[j]):
                return False
            
        return True

