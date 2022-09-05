my_list = [x for x in [1, 2, 3]]
print(my_list)

# --------------------------------------------------
my_list = [x**2 for x in [1, 2, 3]]
print(my_list)

my_tuple = [x**2 for x in {1, 2, 3}]
print(my_tuple)

my_set = {x**2 for x in (1, 2, 3)}
print(my_set)

my_dict = {x: x**2 for x in (1, 2, 3)}
print(my_dict)

# --------------------------------------------------
my_list = [x for x in [1, 2, 3, 4] if x % 2 == 0]
print(my_list)


# --------------------------------------------------
my_list = [x if x % 2 == 0 else x * 100 for x in [1, 2, 3, 4]]
print(my_list)

# --------------------------------------------------
my_list = "".join([chr(ord(x) + 1) for x in reversed("nkkdg".upper())])
print(my_list)
