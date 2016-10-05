n = raw_input()
numbers = map(int, raw_input().strip().split())
sortednumbers = sorted(set(numbers),reverse=True)
print sortednumbers[1]
