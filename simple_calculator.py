import tkinter as tk

def append_character(char):
    current = display_var.get()
    display_var.set(current + str(char))


def clear_display():
    display_var.set("")


def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception:
        display_var.set("Error")


root = tk.Tk()
root.title("Rifat's Simple Calculator")
root.resizable(False, False)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

display_var = tk.StringVar()
entry = tk.Entry(frame, textvariable=display_var, width=16, font=("Arial", 24), bd=4, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=(0, 10))

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    action = (lambda char=text: append_character(char)) if text not in ('C',) else clear_display
    tk.Button(frame, text=text, width=4, height=2, font=("Arial", 18), command=action).grid(row=row, column=col, padx=5, pady=5)

equals_button = tk.Button(frame, text='=', width=18, height=2, font=("Arial", 18), command=calculate)
equals_button.grid(row=5, column=0, columnspan=4, pady=(5, 0))

root.mainloop()

