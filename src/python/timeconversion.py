#!/bin/python

import sys
from datetime import datetime

time = raw_input().strip()
d = datetime.strptime(time,"%I:%M:%S%p")
print d.strftime("%H:%M:%S")
