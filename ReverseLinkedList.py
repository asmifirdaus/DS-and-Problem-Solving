#https://leetcode.com/problems/reverse-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #curr=head
        prev=None
        #nextcurr=head
        curr=head
        #print(prev.val)
        #print(curr.val)
       # print(nextcurr.val)
     
        while(curr):
            nextcurr=curr.next
            curr.next=prev
            prev=curr
            curr=nextcurr
           # print("curr",curr.val)
           # print("next:",nextcurr.val)

        return prev


