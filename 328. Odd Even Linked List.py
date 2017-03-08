# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = None
        odd_head = None
        even = None
        even_head = None
        index = head
        flag = -1
        while index:
            if flag == -1:
                if odd == None:
                    odd_head = index
                    odd = index
                else:
                    odd.next = index
                    odd = odd.next
            else:
                if even == None:
                    even_head = index
                    even = index
                else:
                    even.next = index
                    even = even.next
                #even.next = None
            flag *= -1
            #print(index.val)
            index = index.next
        #print('...')
        if head == None or head.next == None:
            return head
        even.next = None
        #print(odd.val)
        #print(even_head.val)
        #while
        odd.next = even_head
        print(odd_head.val)
        print(odd_head.next.val)
        print(even_head.val)
        #print(even_head.next.val)
        #print(even_head.next.next.val)
        return odd_head