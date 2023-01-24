#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

#Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = None

        if(list1!=None and list2!=None and list1.val <= list2.val):
            head = list1
            list1 = list1.next
        elif(list1!=None and list2!=None and list1.val > list2.val):
            head = list2
            list2 = list2.next
        elif(list1!=None and list2==None):
            head = list1
            list1 = list1.next
        elif(list1==None and list2!=None):
            head = list2
            list2 = list2.next
        else: return None
        current = head
        head2 = head
        while(list1 !=None and list2!= None):
            if(list1.val <= list2.val):
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next
        if(list1!=None and list2==None):
            while(list1!=None):
                current.next = list1
                current = current.next
                list1 = list1.next
        if(list2!=None): 
            while(list2!=None):
                current.next = list2
                current = current.next
                list2 = list2.next
        return head2