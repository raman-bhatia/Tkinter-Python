import tkinter as tk
window = tk.Tk()
window.title("My first GUI App")
window.geometry("1000x600")

mylabel = tk.Label(text = "Hello World")
mylabel.grid(column=0, row=0)

window.mainloop()