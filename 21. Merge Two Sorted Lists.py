# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        index1 = l1
        index2 = l2
        pre2 = l2
        while index1:
            print('2...')
            while index2:
                if index1.val > index2.val:
                    pre2 = index2
                    index2 = index2.next
                    continue
                else:
                    if index2 == l2:
                        print('1....')
                        l2 = index1
                        index1 = index1.next
                        l2.next = index2
                        pre2 = l2
                    else:
                        pre2.next = index1
                        index1 = index1.next
                        pre2.next.next = index2
                        pre2 = pre2.next
                    break
            if index2 is None:
                pre2.next = index1
                break
        return l2
