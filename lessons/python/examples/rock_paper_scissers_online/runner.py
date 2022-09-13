import sys
from subprocess import Popen as po


server = po([sys.executable, sys.path[0] + "/server.py", "", ""])
players = [
    po([sys.executable, sys.path[0] + "/player.py", "", ""], shell=False)
    for _ in range(0, 6)
]

server.wait()
for player in players:
    player.wait()
