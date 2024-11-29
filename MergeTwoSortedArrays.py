#https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merg=ListNode()
        dum=merg
        while(list1 and list2):
            if(list1.val<list2.val):
                dum.next=list1
                list1=list1.next
            else:
                dum.next=list2
                list2=list2.next
            dum=dum.next
        if(list1):
            dum.next=list1
            #list1=list1.next
        elif(list2):
            dum.next=list2
        return merg.next
