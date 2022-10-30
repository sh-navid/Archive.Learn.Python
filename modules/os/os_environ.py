import os

env=os.environ

print(type(env))

for key in env:
    print(key)

print("-"*30)

print(env["LANG"])