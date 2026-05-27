# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        l=0
        while curr:
            l+=1
            curr=curr.next
        dist=l-n
        if dist==0:
            return head.next
        curr=head
        for i in range(dist-1):
            curr=curr.next
        curr.next=curr.next.next if curr.next else None
        return head
        
        