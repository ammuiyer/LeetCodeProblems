#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #implementing a stack as a list but not rlly
        #treating list as a stack?
        i = 0
        stack = []
        while i<len(s):
            if(self.isopenDelimeter(s[i])):
                stack.append(s[i])
            elif(self.isclosedDelimeter(s[i])):
                if(len(stack)==0): return False
                if(self.isMatching(stack.pop(),s[i]) == False): 
                    return False
            i = i+1
        if len(stack)!=0: return False
        return True
    def isMatching(self, a, b):
        if (a=="(" and b == ")"): return True
        elif (a=="[" and b == "]"): return True
        elif (a=="{" and b == "}"): return True
        return False
    def isopenDelimeter(self, a):
        if (a == "("): return True
        elif (a == "["): return True
        elif (a == "{"): return True
        else: return False
    def isclosedDelimeter(self, a):
        if (a == ")"): return True
        elif (a == "]"): return True
        elif (a == "}"): return True
        else: return False
