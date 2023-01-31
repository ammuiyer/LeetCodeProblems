# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

#For each index i, names[i] and heights[i] denote the name and height of the ith person.

#Return names sorted in descending order by the people's heights.

class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """

        for outer in range (1,len(heights)): 
            temp = heights[outer]  
            temp2 = names[outer]            
            i = outer
            while i>0 and (heights[i-1]<temp):      
                heights[i] = heights[i-1] 
                names[i] = names[i-1] 
                i=i-1
            heights[i] = temp    
            names[i] = temp2
        return names

