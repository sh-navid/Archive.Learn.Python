import os
import sys
import time


p = os.path.join(sys.path[0], "os_remove.txt")
q = os.path.join(sys.path[0], "os_remove2.txt")
open(p, "w+").close()


time.sleep(5)
os.rename(p,q)


time.sleep(5)
os.remove(q)