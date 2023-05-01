import tkinter as tk

# def hello(event):
    # print("Hello World!")

window = tk.Tk()
window.title("My first GUI App")
window.geometry("1000x600")

myEntry = tk.Entry(window)
myEntry.grid(column=0, row=0)

# mylabel = tk.Label(text = "Hello World")
# mylabel.grid(column=0, row=0)
# mylabel.pack(side=tk.TOP)

# mylabel2 = tk.Label(text = "How are you?")
# mylabel2.grid(column=1, row=1)

# mybutton = tk.Button(window, text = "Click Me")
# mybutton.grid(column=0, row=1)
# mybutton.bind("<Button-1>", hello)

window.mainloop()