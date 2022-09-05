for x in [4, 5, 6, 7, 8, 9, 10, 11, 12]:
    if x < 7:
        continue
    print(x)
    if x > 10:
        break
print()

# --------------------------------------------------
for x in "STRING":
    print(x)
print()

# --------------------------------------------------
x = [2, 3, 4]
y = [22, 33, 44]
for a, b in zip(x, y):
    print(a, b)
print()

# --------------------------------------------------
for x in range(10,30,5):
    print(x)
print()

# --------------------------------------------------
for i,x in enumerate(["A","B","C"]):
    print(i,x)