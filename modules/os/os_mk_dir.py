import os
import sys
import time

try:
    os.mkdir(os.path.join(sys.path[0], "my_dir"))
except:
    print("Path exists")

time.sleep(5)

os.rmdir(os.path.join(sys.path[0], "my_dir"))
