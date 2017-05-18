# there are two solutions: iterative and recursive
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        a = []
        while hasattr(self, 'value'):
            a.append(str(self.value))
            self = self.next
        return ''.join(a)


class Solution:
    def reverseListIterative(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            # a simple trick : head.next, head, prev = prev, head.next, head
        return prev

    def reverseListRecursive(self, head, prev=None):
        if not head:
            return prev
        next = head.next
        head.next = prev
        return self.reverseListRecursive(next, head)

if __name__ == '__main__':
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l2 = ListNode(7)
    l2.next = ListNode(8)
    l2.next.next = ListNode(9)
    a = Solution()
    print 'origin linked list {}'.format(l1)
    print 'after iterative solution {}'.format(a.reverseListIterative(l1))
    print 'origin linked list {}'.format(l2)
    print 'after recursive solution {}'.format(a.reverseListRecursive(l2))
