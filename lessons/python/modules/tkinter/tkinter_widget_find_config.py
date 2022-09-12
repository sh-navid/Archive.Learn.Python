from tkinter import Button

button = Button()

print(set(dir(button)))

print("-" * 79)

print(set(button.configure().keys()))




