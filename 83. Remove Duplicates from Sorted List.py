# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        index = head
        while index:
            if index.next is not None and index.next.val == index.val:
                index.next = index.next.next
                continue
            index = index.next
        return head
