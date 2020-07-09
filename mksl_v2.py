# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List

class Solution:

    def add_node(self, l: ListNode) -> ListNode:
        node = ListNode(l.val)
        self.tail.next = node 
        self.tail = node
        return l.next

    def merge2Lists(self, list1: List[ListNode], list2: List[ListNode]):
        self.head = ListNode(0)
        self.tail = self.head

        while True:
            if list1 is None:
                if list2 is None:
                    return self.head.next
                list2 = self.add_node(list2)
            elif list2 is None:
                list1 = self.add_node(list1)
            elif list1.val < list2.val:
                list1 = self.add_node(list1)
            else:
                list2 = self.add_node(list2)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        if k == 0:
            return None 
        elif k == 1:
            return lists[0]
        elif k == 2:
            return self.merge2Lists(lists[0], lists[1])
        else:
            half = k // 2
            lists0 = self.mergeKLists(lists[0:half])
            lists1 = self.mergeKLists(lists[half:])
            return self.merge2Lists(lists0, lists1)
      
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
