# tk18.pyw

import tkinter as tk
def print_txtval():
    val_en = en.get()
    en.delete(0, tk.End)
    print(val_en)


root = tk.Tk()
en = tk.Entry()
en.insert(0, 'original')
bt = tk.Button(text='ボタン', command=print_txtval)
[widget.pack() for widget in (en, bt)]
en.focus_set()
root.mainloop()
