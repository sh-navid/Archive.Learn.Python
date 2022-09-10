from tkinter import simpledialog

answer = simpledialog.askfloat("Ask Float", "Ask for float number?")
print("askfloat", answer)

answer = simpledialog.askinteger("Ask Integer", "Ask for int number?")
print("askinteger", answer)

answer = simpledialog.askstring("Ask Integer", "Ask for string?")
print("askstring", answer)
