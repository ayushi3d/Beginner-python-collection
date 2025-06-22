import tkinter as tk
import math

# Colors and font
BG_COLOR = "#FFF5F8"
BTN_COLOR = "#FFB6C1"
BTN_FONT = ("Comic Sans MS", 16)
ENTRY_FONT = ("Arial Rounded MT Bold", 22)


def press(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def power():
    entry.insert(tk.END, "**")


# Create window
root = tk.Tk()
root.title("💖 Cute Calculator")
root.configure(bg=BG_COLOR)
root.geometry("340x450")
root.resizable(False, False)

# Entry
entry = tk.Entry(root, font=ENTRY_FONT, bd=5, bg="white", relief="groove", justify='right')
entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=10, padx=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
    ('C', 5, 0), ('√', 5, 1), ('^', 5, 2)
]

# Button creator
for (text, row, col) in buttons:
    if text == "=":
        cmd = calculate
    elif text == "C":
        cmd = clear
    elif text == "√":
        cmd = sqrt
    elif text == "^":
        cmd = power
    else:
        cmd = lambda t=text: press(t)

    b = tk.Button(root, text=text, bg=BTN_COLOR, font=BTN_FONT, padx=20, pady=10, command=cmd, relief="groove", bd=2)
    b.grid(row=row, column=col, padx=5, pady=5)

# Fill extra space with blank label
tk.Label(root, text="", bg=BG_COLOR).grid(row=6, column=0, columnspan=4)

# Run app
root.mainloop()



