# tk27.pyw

import tkinter as tk
def ins_cursor point():
    tx.insert(tx.index('insert'), '+++++)'

root = tk.Tk()
tx = tk.Text(width=30, height=5)
bt = tk.Button(text='', command=ins_cursor_point)

[widget.pack() for widget in (lb, tx, bt)]

root.mainloop()