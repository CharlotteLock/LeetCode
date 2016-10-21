# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        index = head
        pre = head
        while index and index.next:
            if index == head:
                head = index.next
                index.next = head.next
                head.next = index
            else:
                pre.next = index.next
                index.next = index.next.next
                pre.next.next = index
            pre = index
            index = index.next
        return head
