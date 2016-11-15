# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        index = head
        tmp = index.next
        while tmp:
            if index == head:
                index.next = None
            tmp.next, index, tmp = index, tmp, tmp.next
        return index
