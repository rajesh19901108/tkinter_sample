# tk30.pyw

import tkinter as tk

def get_ckval():
    lb['text'] = 'Checked' if boolvar.get() else 'Not checked'

root = tk.Tk()
root.geometry('250x100')
boolvar = tk.BooleanVar()
lb = tk.Label()
ck = tk.Checkbutton(text='checkbox', variable = boolvar)
bt = tk.Button(text = '判定', command = get_ckval)
[widget.pack() for widget in (lb, ck, bt)]
root.mainloop()