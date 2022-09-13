import sys

with open(sys.path[0]+"/test-file.txt","w") as file:
    file.write("Hello File")

with open(sys.path[0]+"/test-file.txt","r") as file:
    print(file.readlines())