import tkinter as tk

def print_txtval():
    val_en = en.get()
    print(val_en)

root = tk.Tk()
root.title('Get text box')
root.geometry('350x150')
lb = tk.Label(text = 'Label-1')
en = tk.Entry()
bt = tk.Button(text = 'Button-1',command = print_txtval)
lb.pack()
en.pack()
bt.pack()
root.mainloop()