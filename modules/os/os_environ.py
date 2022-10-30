import os

env = os.environ

print(type(env))

for key in env:
    print(key)

print("-"*30)

print(env["LANG"])
print(env["OS"])
print(env["HOMEPATH"])
print(env["APPDATA"])
print(env["SYSTEMDRIVE"])
print(env["WINDIR"])
