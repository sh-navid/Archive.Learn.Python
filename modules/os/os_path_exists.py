import os
import sys

print(os.path.exists(sys.path[0]))
print(os.path.exists(sys.path[0]+"/a.txt"))
print(os.path.exists(sys.path[0]+"/os_name.py"))
