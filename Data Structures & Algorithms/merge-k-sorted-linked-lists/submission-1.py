# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
            res=ListNode(0)
            dummy=res
            while list1 and list2:
                if list1.val>list2.val:
                    res.next=list2
                    list2=list2.next
                else:
                    res.next=list1
                    list1=list1.next
                res=res.next
            res.next=list1 if list1 else list2
            return dummy.next
        def divide(lists, l, r):
            if l>r:
                return None
            if l==r:
                return lists[l]
            mid=l+(r-l)//2
            left=divide(lists, l, mid)
            right=divide(lists, mid+1, r)

            return merge(left, right)

        if not lists or len(lists)==0:
            return None
        return divide(lists, 0, len(lists)-1)
