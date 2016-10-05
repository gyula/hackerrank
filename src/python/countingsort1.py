import sys

list_size = int(raw_input())
in_list = raw_input().split(" ")
res = [0] * 100
for i in range(0,list_size):
    res[int(in_list[i])] += 1
for i in res: sys.stdout.write("%s " % i)
