D = {
    "Key1": "Value1",
    "Key2": "Value2",
    "Key3": "Value3",
    "Key4": "Value4",
    "Key6": "Value6",
    "Key7": "Value7",
    "Key8": "Value8",
}

M={}

for k, v in D.items():
    M[v] = k


print(D)
print(M)
