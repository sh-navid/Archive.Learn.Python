from enum import Enum, auto
import sys


tasks = []

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 2 <-----
class Importance(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class Task:
    title = None
    description = None
    is_done = False
    importance = None

    def __init__(self, title, description, importance=Importance.MEDIUM) -> None:
        self.title = title
        self.description = description
        ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Answer 2 <-----
        self.importance = importance

    def done(self):
        self.is_done = True

    def __str__(self) -> str:
        done = "x" if self.is_done else "-"
        return f"[{done}] {self.title.ljust(15)} '{self.description.ljust(30)}', {self.importance.name}"

    def __repr__(self) -> str:
        return self.__str__()

tasks.append(Task("Buy", "Buy soda for dinner"))
tasks.append(Task("Gym", "Go to gym", importance=Importance.LOW))
tasks.append(Task("Mail", "Send mail to Office", importance=Importance.HIGH))
tasks.append(Task("Wash your Car", ""))
tasks.append(Task("Buy", "Buy a pen"))
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 1 <-----
tasks.append(Task("Buy", "Buy a car"))
tasks.append(Task("Buy", "Buy a phone"))

tasks[1].done()
tasks[2].done()

# for task in tasks:
#    print(task)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 3 <-----
L, c = len(tasks), 0
while c < L:
    print(tasks[c])
    c += 1

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 4 <-----
with open(sys.path[0]+"/temp.txt","w") as file:
    file.write(str(tasks))