#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1, c2 = l1, l2
        head = ListNode((c1.val + c2.val) % 10 )
        carry = (c1.val + c2.val)//10
        current = head
        while c1.next or c2.next:
            if c1.next and c2.next:
                c1, c2 = c1.next, c2.next
                s = int(c1.val + c2.val + carry)
            elif c1.next:
                c1 = c1.next
                s = int(c1.val + carry)
            else:
                c2 = c2.next
                s = int(c2.val + carry)
            current.next = ListNode(int(s % 10))
            carry = s // 10
            current = current.next
        if carry:
            current.next = ListNode(carry)
        return head

def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def print_linked_list_in_order(head):
    current = head
    while current:
        print(int(current.val))
        current = current.next


print_linked_list_in_order(Solution().addTwoNumbers(array_to_linked_list([2,4,3]), array_to_linked_list([5,6,4])))
