import re
IPv4 = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
IPv6 = r'^([0-9A-Fa-f]{0,4}:){2,7}([0-9A-Fa-f]{1,4}$|((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4})$'
n = int(raw_input().strip())
for i in range(n):
    line = raw_input().strip()
    if (re.match(IPv4, line)):
        print "IPv4"
    elif (re.match(IPv6, line)):
        print "IPv6"
    else:
        print "Neither"
