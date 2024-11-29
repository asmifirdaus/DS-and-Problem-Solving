#https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # dummy = node = ListNode(0)
        # h = [(n.val, n) for n in lists if n]
        # heapify(h)
        # while h:
        #     v, n = h[0]
        #     if n.next is None:
        #         heappop(h) #only change heap size when necessary
        #     else:
        #         heapreplace(h, (n.next.val, n.next))
        #     node.next = n
        #     node = node.next

        # return dummy.next

        h = []
        head = tail = ListNode(0)
        for i in lists:
            if i:
                heapq.heappush(h, (i.val, i))

        while h:
            node = heapq.heappop(h)[1]
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(h, (node.next.val, node.next))

        return head.next

        
