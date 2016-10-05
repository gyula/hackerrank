#!/bin/python

import sys
lefts = '{[('
rights = '}])'
brackets = { a:b for a,b in zip(rights,lefts)}

def isBalanced(s):
    br_stack = []
    for c in s:
        if c in lefts:
            br_stack.append(c)
        elif c in rights:
            if not br_stack or br_stack.pop() != brackets[c]:
                return False
    return not br_stack

t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    if isBalanced(s):
        print 'YES'
    else:
        print 'NO'
