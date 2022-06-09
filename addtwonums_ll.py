# Definition for singly-linked list.
class ListNode(object):
        def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        temp = ListNode()
        cur = temp
        
        carry = 0
        # when v1 or v2 only has 1 node and has a carry when added
        # v1 and v2 is None, but carry has a value of 1,
        # the loop will end, thefore make a third condition
        #
        while l1 or l2 or carry:
            #checks if v1 or v2 has a value else 0
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0
            
            #new digit
            val = v1 + v2 + carry  
            carry = val // 10 #for ex: 13 // 10 = 1 or 20 // 2 = 2
            val = val % 10  #do this because if the val > 10
            cur.next = ListNode(val)
            
            #update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return temp.next
        
        