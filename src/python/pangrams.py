import re
from collections import Counter
instring = raw_input().strip()
chars = re.findall(r'\S', instring.lower())
cnt = Counter(chars)
if len(cnt) == 26:
    print "pangram"
else:
    print "not pangram"
