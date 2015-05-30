#there are two solutions: iterative and recursive
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        a = []
        while hasattr(self,'value'):
            a.append(str(self.value))
            self = self.next
        return ''.join(a)

class Solution:
    def reverseListIterative(self, head):
        prev = None
        while head:
            curr = head
            curr.next = prev
            head = head.next
            prev = curr
        return prev

    def reverseListRecursive(self, head, prev=None):
        if not node:
            return prev
        head = head.next
        head.next = prev
