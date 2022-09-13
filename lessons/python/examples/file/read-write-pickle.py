import pickle
import sys


class Person:
    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name

    def __str__(self) -> str:
        return ", ".join((self.name, self.last_name))


my_list = [Person("N1", "F1"), Person("N2", "F2")]


with open(sys.path[0] + "/test-file-pickle.txt", "wb") as file:
    file.write(pickle.dumps(my_list))

del my_list

with open(sys.path[0] + "/test-file-pickle.txt", "rb") as file:
    my_list = pickle.loads(file.read())


for item in my_list:
    print(item)
