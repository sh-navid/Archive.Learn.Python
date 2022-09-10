import random

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer1
my_list = [2, 4, 6]
for i, item in enumerate(my_list):
    my_list[i] = item * 2
print(my_list)
"""
[4, 8, 12]
"""

# OR

my_list = [2, 4, 6]
for i in range(len(my_list)):
    my_list[i] *= 2
print(my_list)
"""
[4, 8, 12]
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer2
user_list = ["user1", "user2", "user3"]
pass_list = ["pass1", "pass2", "pass3"]

u = input("Enter username: ").strip()
p = input("Enter password: ").strip()

found = False
for user, password in zip(user_list, pass_list):
    if u == user and p == password:
        found = True
        break

if found:
    print("Founded")
else:
    print("Not Found")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer3
num_list = [2.1, 4.6, 5.7, 8.9, 9.1, 0.3]
for i, item in enumerate(num_list):
    num_list[i] = item // 1
print(num_list)
"""[2.0, 4.0, 5.0, 8.0, 9.0, 0.0]"""

for i, item in enumerate(num_list):
    num_list[i] = item + 1
print(num_list)
"""[3.0, 5.0, 6.0, 9.0, 10.0, 1.0]"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer4
my_list = [0, 50, 100, 150, 200, 250]
for i in range(len(my_list)):
    my_list[i] = bin(my_list[i])
    my_list[i] = my_list[i].replace("0b", "")
    my_list[i] = my_list[i].zfill(8)
print(my_list)
"""['00000000', '00110010', '01100100', '10010110', '11001000', '11111010']"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer5
my_list = ["00000000", "00110010", "01100100", "10010110", "11001000", "11111010"]
for i in range(len(my_list)):
    my_list[i] = int(my_list[i], 2)
print(my_list)
"""[0, 50, 100, 150, 200, 250]"""
