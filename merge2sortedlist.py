# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        temp = ListNode()
        cur = temp 
        
        while list1 or list2:
            v1 = list1.val if list1 else None 
            v2 = list2.val if list2 else None
            
            if v1 is None and v2 is None:
                cur.next = ListNode()
                list1 = list1.next if list1 else None
                list2 = list2.next if list2 else None
            elif v2 is None:
                cur.next = ListNode(v1)
                list1 = list1.next if list1 else None        
            elif v1 is None:
                cur.next = ListNode(v2)
                list2 = list2.next if list2 else None  
            else:
                if v1 > v2:
                    cur.next = ListNode(v2)
                    list2 = list2.next if list2 else None
                else:
                    cur.next = ListNode(v1)
                    list1 = list1.next if list1 else None

            #update pointers
            
            cur = cur.next
        return temp.next