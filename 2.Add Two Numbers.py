# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        top = 0
        result.val = (l1.val + l2.val) % 10 + top
        top = (l1.val + l2.val) // 10
        result_ind = result
        while l1.next or l2.next:
            if l1.next:
                l1 = l1.next
            else:
                l1.val = 0
            if l2.next:
                l2 = l2.next
            else:
                l2.val = 0
            tmp = ListNode(0)
            result_ind.next = tmp
            result_ind = result_ind.next
            result_ind.val = (l1.val + l2.val + top) % 10
            top = (l1.val + l2.val + top) // 10
        if top:
            result_ind.next = ListNode(top)
        return result
