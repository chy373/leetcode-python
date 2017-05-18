#!/usr/bin/env python
# encoding: utf-8

'''
21. Merge Two Sorted Lists
Difficulty: Easy Tags: Linked List

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    # iteratively
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1

        if l2:
            head.next = l2
        return dummy.next

    # recursively
    def mergeTwoLists_r(self, l1, l2):
        if not l1:
            return l1
        if not l2:
            return l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists_r(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_r(l2.next, l1)
            return l2
