from tkinter import messagebox

answer = messagebox.askretrycancel(title="Retry Cancel",message="My msg...")
print("askretrycancel", answer)

answer = messagebox.askquestion(title="Question",message="My question...")
print("askquestion", answer)

answer = messagebox.askokcancel(title="Ok Cancel",message="My msg...")
print("askokcancel", answer)

answer = messagebox.askyesno(title="Yes No",message="My msg...")
print("askyesno", answer)

answer = messagebox.askyesnocancel(title="Yes No Cancel",message="My msg...")
print("askyesnocancel", answer)
