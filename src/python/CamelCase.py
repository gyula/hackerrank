instring = raw_input().strip()
print sum(1 for c in instring if c.isupper())+1
