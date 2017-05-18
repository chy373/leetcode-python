'''
Problem: Integer Break
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Solution:
Given an integer let's say there is a possible product P=p1*p2*...pn, if we break the integer into two items, 2 and pi-2
if 2(pi-2)>pi ==> pi>4, so we will get a bigger product if pi > 4, likewise 3(pi>4.5)

so we can get biggest product if


'''
