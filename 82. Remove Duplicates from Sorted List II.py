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
        pre = index
        tag = 0
        while index:
            if index.next is not None:
                if index.next.val == index.val:
                    tag = 1
                    index.next = index.next.next
                    continue
                else:
                    if tag:
                        if index != head:
                            pre.next = index.next
                            index = index.next
                        else:
                            index = index.next
                            head = index
                            pre = head
                        tag = 0
                    else:
                        index = index.next
                        if index != head.next:
                            pre = pre.next
            else:
                if tag:
                    if index != head:
                        pre.next = None
                    else:
                        head = None
                    break
                else:
                    index = index.next
        return head
