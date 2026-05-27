# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next

        index=l-n
        if index==0:
            return head.next

        curr=head
        for i in range(l-1):
            if (i+1)==index:
                curr.next=curr.next.next
                break
            curr=curr.next
        return head
