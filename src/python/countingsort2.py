import sys
n = raw_input()
s = list(raw_input().split(" "))
s.sort(key=int)
for item in s : sys.stdout.write(item + " ")
