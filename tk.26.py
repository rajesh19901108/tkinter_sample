# tk26.pyw

import tkinter as tk

def print_selpoint():
    sel_start = tx.index('sel.first')
    sel_end = tx.index('sel.last')
    print(tx.get(sel_start, sel_end))

root = tk.Tk()
tx = tk.Text(width=30, height=5)
bt = tk.Button(text='selected range', command=print_selpoint)

[widget.pack() for widget in (lb, tx, bt)]

root.mainloop()