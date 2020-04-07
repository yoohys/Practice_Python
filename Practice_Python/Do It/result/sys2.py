#sys2.py

import sys
args=sys.argv[1:]
for i in args:
    print(i.upper(),end=' ')
    
#         argv[0]   argv[1]   argv[2]   argv[3]
# python  sys1.py   aaa       bbb       ccc