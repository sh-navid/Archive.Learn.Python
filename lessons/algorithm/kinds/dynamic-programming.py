# Dynamic Programming + Recursive Algorithm

dynamic = {}


def fibo_recursive(a):
    if a <= 2:  # Here index is from 1
        return 1
    else:
        f = None
        if a in dynamic:
            f = dynamic[a]
            # print(f"Store: {a}->{f}")
        else:
            f = fibo_recursive(a - 2) + fibo_recursive(a - 1)
            dynamic[a] = f
            # print(f"Restore: {a}->{f}")
        return f


# Index -> 1 2 3 4 5 6 7   8   9
# Value -> 1 1 2 3 5 8 13  21  34

for i in range(1, 10000):
    print(f"Fibo {i}: {fibo_recursive(i)}")
