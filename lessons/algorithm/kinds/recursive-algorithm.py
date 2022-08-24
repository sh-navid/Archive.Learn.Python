# Recursive Algorithm


def fibo_recursive(a):
    print(f"Fibo {a} is executed right now")
    if a <= 2:  # Here index is from 1
        print(f"Fibo {a} is equal to {1}")
        return 1
    else:
        sum = fibo_recursive(a - 2) + fibo_recursive(a - 1)
        print(f"Fibo {a} is equal to {sum}")
        return sum


# Index -> 1 2 3 4 5 6 7   8   9
# Value -> 1 1 2 3 5 8 13  21  34

# for i in range(1, 5):
#    print(f"Fibo {i}: {fibo_recursive(i)}")

print(fibo_recursive(5))

# We can optimize this process with "Dynamic Programmig and Storing the data in Array"