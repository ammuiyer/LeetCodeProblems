#Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        counter = 0
        current = head
        prev = None
        n = self.length(head)-n
        while(counter!=n):
            prev = current
            current = current.next
            counter = counter + 1
        
        print(current.val)
        if(counter ==0):
            head = head.next
        elif(current.next==None):
            prev.next = None
        else:
            prev.next = current.next
        return head
    def length(self, head):
        current = head
        counter = 0
        while(current!=None):
            current = current.next
            counter = counter+1
        return counter
