# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        resultHead = None
        resultTail = None
        carry = 0
        while l1 or l2:
            total = carry
            if l2:
                total = total + l2.val
                l2 = l2.next
            if l1:
                total = total + l1.val
                l1 = l1.next

            carry = total // 10 # 15 // 10 = 1; 6 // 10 = 0
            total = total % 10  # 15 % 10 = 5; 6 % 10 = 6

            if not resultHead: # this is the first result node
                resultHead = ListNode(total, None)
                resultTail = resultHead 
            else:
                temp = ListNode(total, None)
                resultTail.next = temp
                resultTail = temp
        if carry == 1:
            resultTail.next = ListNode(carry, None)
                
        return resultHead