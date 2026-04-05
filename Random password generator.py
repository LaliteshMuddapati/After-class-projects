import tkinter as tk
import random
letters = ['1','2','3','4','5','6','7','8','9','0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
window = tk.Tk()
i = tk.Entry(window, width=100)
def password():
    l = i.get()
    s = ""
    for j in range(int(l)):
        s += random.choice(letters)
    i.delete(0, tk.END)
    i.insert(0, s)
b = tk.Button(window, text="Generate", command=password, width=100, height=1)
i.pack()
b.pack()

window.mainloop()