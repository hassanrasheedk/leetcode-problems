# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        numstring1 = []
        numstring2 = []
        
        while l1 is not None:
            numstring1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            numstring2.append(l2.val)
            l2 = l2.next
        
        numstring1.reverse()
        numstring2.reverse()
        
        str1 = ''.join(str(e) for e in numstring1)
        str2 = ''.join(str(e) for e in numstring2)
        
        resultstring = int(str1) + int(str2)
        
        resultstring = str(resultstring)
        
        lr = ListNode()
        head = lr
        
        for c in reversed(resultstring):
            lr.next = ListNode(c)
            lr = lr.next
        
        return head.next
