# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        index = head
        length = 1
        while index.next:
            length += 1
            index = index.next
        if length == n :
            if n != 1:
                return head.next
            else:
                return None
        index = head
        for i in range(length - n -1):
            index = index.next
        index.next = index.next.next
        return head
