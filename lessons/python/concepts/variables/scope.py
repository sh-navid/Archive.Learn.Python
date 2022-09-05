a = 12
b = 13


def show():
    global a
    c = 300
    w = 100

    def inner():
        nonlocal w
        w = 200
        u = 35

        print("\nLocals   for 'inner':")
        print([" = ".join([str(k), str(v)]) for k, v in locals().items() if not k.startswith("__")])

        print("\nGlobals  for 'inner':")
        print([" = ".join([str(k), str(v)]) for k, v in globals().items() if not k.startswith("__")])

    inner()

    print("\nLocals   for 'show':")
    print([" = ".join([str(k), str(v)]) for k, v in locals().items() if not k.startswith("__")])

    print("\nGlobals  for 'show':")
    print([" = ".join([str(k), str(v)]) for k, v in globals().items() if not k.startswith("__")])

show()
