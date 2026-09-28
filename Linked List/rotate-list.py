# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        curr = head
        length = 0
        while curr:
            length += 1
            if curr.next is None:
                curr.next = head
                break
            curr = curr.next
        tail = length - (k % length)
        curr = head
        for i in range(tail - 1):
            curr = curr.next       
        head = curr.next
        curr.next = None  
        return head