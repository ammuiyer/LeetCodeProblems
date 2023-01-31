#took me 3 days :/
#Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # find the left and what is before hte lefts
        current = head
        prev = None
        counter = 1
        while(counter<left and current is not None):
            prev = current
            current = current.next
            counter = counter + 1
        current2 = current
        while(counter<right and current2 is not None):
            current2 = current2.next
            counter = counter + 1
        if(prev!=None):
            next = current2.next
            temp = current
            while(left<=right):
                temp = current
                current = current.next
                temp.next = next
                next = temp
                left = left+1
            prev.next = temp
        else:
            next = current2.next
            temp = current
            while(left<=right):
                temp = current
                current = current.next
                temp.next = next
                next = temp
                left = left+1
            return temp
        return head