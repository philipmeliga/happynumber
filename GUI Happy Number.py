import tkinter as tk

def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1

def check_happy_number():
    num = int(entry.get())
    result = is_happy_number(num)
    label_result.config(text=f"{num} is happy number" if result else f"{num} is sad number")

root = tk.Tk()
root.title("Happy Number Checker")

label = tk.Label(root, text="Enter a number:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Check", command=check_happy_number)
button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()