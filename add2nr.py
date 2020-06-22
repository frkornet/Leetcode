# Leetcode:
#
# 2. Add Two Numbers (Medium)
#
# You are given two non-empty linked lists representing two non-negative 
# integers. The digits are stored in reverse order and each of their 
# nodes contain a single digit. Add the two numbers and return it as a 
# linked list.
#
# You may assume the two numbers do not contain any leading zero, except 
# the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_ptr = None
        last_ptr  = None
        carry = 0
        while (l1 or l2):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = val1 + val2 + carry
            carry = value // 10
            value = value % 10
            node = ListNode(value, None)

            if first_ptr == None:
                first_ptr = node

            if last_ptr:
                last_ptr.next = node
            last_ptr = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry > 0:
            node = ListNode(carry, None)
            last_ptr.next = node

        return first_ptr

def number_to_string(l1: ListNode):
    number_str = ""
    first_elem = True
    while l1:
        value = l1.val
        l1 = l1.next
        if first_elem == False:
            number_str += " -> "
        number_str += str(value)
        first_elem = False
    return number_str

def create_list(value) -> ListNode:
    assert value >= 0, "value must be non-negative!"
    first_ptr = None
    last_ptr = None
    while (True):
        digit = value % 10
        value = value // 10

        node = ListNode(digit, None)

        if first_ptr == None:
            first_ptr = node

        if last_ptr:
            last_ptr.next = node
        last_ptr = node

        if value == 0:
            break

    return first_ptr

def test_two_numbers(l1: ListNode, l2: ListNode) -> bool:
    
    while l1 or l2:
        if (l1.next == None and l2.next) or (l2.next == None and l1.next):
            return False

        if l1.val != l2.val:
            return False
    
        l1 = l1.next
        l2 = l2.next

    return True

test_samples = [ (342, 465, 807), 
                 (342, 865, 1207),
                 (34, 512, 546),
                 (38, 512, 550),
                 (111, 999, 1110),
                  ]

i = 0
for val1, val2, e_val in test_samples:
    l1 = create_list(val1)
    l2 = create_list(val2)
    ea = create_list(e_val)

    l1_str = number_to_string(l1)
    l2_str = number_to_string(l2)
    ea_str = number_to_string(ea)

    soln=Solution()
    soln_list = soln.addTwoNumbers(l1,l2)
    soln_str = number_to_string(soln_list)

    correct = test_two_numbers(ea, soln_list)
    testcase_result = "l1=" + l1_str +" l2=" + l2_str + " ea=" + ea_str \
                    + " soln=" + soln_str + " correct=" + str(correct)

    print(f"testcase {i:02d}: {testcase_result}")
    i += 1

print('Done.')

