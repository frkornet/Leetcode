# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None # empty list
        
        def minimum_index():
            min_idx = -1
            for i, l in enumerate(lists):
                if l is not None and (min_idx == -1 or l.val <= lists[min_idx].val):
                    min_idx = i

            return min_idx == -1, min_idx

        head = tail = ListNode(0)
        while True:
            done, min_idx = minimum_index()
            if done:
                return head.next
            
            node = ListNode(lists[min_idx].val)
            tail.next = node
            tail = node
            lists[min_idx] = lists[min_idx].next
            if lists[min_idx] is None:
                lists.pop(min_idx)
            
node1=ListNode(1)
node2=ListNode(4)
node1.next = node2
node3= ListNode(5)
node2.next = node3
list1 = node1

node4 = ListNode(1)
node5 = ListNode(3)
node4.next = node5
node6 = ListNode(4)
node5.next = node6
list2 = node4

node7 = ListNode(2)
node8 = ListNode(6)
node7.next = node8
list3 = node7

lists=[list1, list2, list3]
print("lists=", lists)

soln = Solution()
result = soln.mergeKLists(lists)
print("result=", result)
print("")
