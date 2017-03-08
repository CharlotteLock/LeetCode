# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        index = head
        prev = head
        mid = head
        while index:
            if index.val < x: 
                if mid != None:
                    if index != mid and index != mid.next:
                        prev.next = index.next
                        mid.next, index.next = index, mid.next
                        index = prev.next
                        mid = mid.next
                        continue
                    elif index == mid.next:
                        mid = mid.next
                else:
                    prev.next = index.next
                    index.next = head
                    head = index
                    mid = index
                    index = prev.next
                    continue
            elif index == head:
                mid = None
            if index != head:
                prev = index
            index = index.next
        return head