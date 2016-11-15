# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        index = head
        pre = head
        while index:
            if index.val == val:
                if index == head:
                    head = index.next
                    pre = head
                else:
                    pre.next = index.next
                index = index.next
            else:
                index = index.next
                if pre.next != index:
                    pre = pre.next
        return head
