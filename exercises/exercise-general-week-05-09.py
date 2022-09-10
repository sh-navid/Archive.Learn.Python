tasks = []

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Task:
    title = None
    description = None
    is_done = False

    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description

    def done(self):
        self.is_done = True

    def __str__(self) -> str:
        done = "x" if self.is_done else "-"
        return f"[{done}] {self.title.ljust(10)} '{self.description}'"


tasks.append(Task("Buy", "Buy soda for dinner"))
tasks.append(Task("Gym", "Go to gym"))
tasks.append(Task("Mail", "Send mail to Office"))
tasks.append(Task("Wash your Car", ""))
tasks.append(Task("Buy", "Buy a pen"))

tasks[1].done()
tasks[2].done()

for task in tasks:
    print(task)
