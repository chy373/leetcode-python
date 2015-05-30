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
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = temp = ListNode(0)
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.value
                l1 = l1.next
            if l2:
                sum += l2.value
                l2 = l2.next
            if carry:
                sum += carry
            carry ,value = divmod(sum,10)
            temp.next = ListNode(value)
            temp = temp.next
            print 'temp {}'.format(temp)
            print 'result {}'.format(result)
        return result.next

if __name__ == '__main__':
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l2 = ListNode(7)
    l2.next = ListNode(8)
    l2.next.next = ListNode(9)
    a = Solution()
    a.addTwoNumbers(l1,l2)
