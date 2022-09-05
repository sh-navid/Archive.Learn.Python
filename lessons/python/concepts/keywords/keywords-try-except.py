try:
    print(1 + "hello")
except Exception as e:  # if error
    print("Error", e)
else:  # if no error
    print("No Error")
finally:
    print("Execute it at last")

# --------------------------------------------------
print("#"*69)

# --------------------------------------------------
try:
    print("hello")
except Exception as e:  # if error
    print("Error", e)
else:  # if no error
    print("No Error")
finally:
    print("Execute it at last")
