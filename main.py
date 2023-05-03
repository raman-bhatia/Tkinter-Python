import tkinter as tk

# def hello(event):
    # print("Hello World!")

window = tk.Tk()
window.title("My Window")
window.geometry("600x400")


mylabel = tk.Label(text = "Enter your name: ")
mylabel.grid(column=0, row=0)
myEntry = tk.Entry(window)
myEntry.grid(column=1, row=0)
# mylabel.pack(side=tk.TOP)

def inputData():
    name = myEntry.get()
    print("The username is " + name)

myButton = tk.Button(window,text = "Submit", command = inputData)
myButton.grid(column=0, row=1)

# mylabel2 = tk.Label(text = "How are you?")
# mylabel2.grid(column=1, row=1)

# mybutton = tk.Button(window, text = "Click Me")
# mybutton.grid(column=0, row=1)
# mybutton.bind("<Button-1>", hello)

window.mainloop()