# tk24.pyw

import tkinter as tk
def get_selpoint():
    sel_start = tx.index('sel.first')
    sel_end = tx.index('sel.last')
    cursor_point = txt.index('insert')
    lb['text'] = 'sel_start:{}, sel_end:{}' cursor:{}.format(sel_start, sel_end, cursor_point)

root = tk.Tk()
lb = tk.Label()
tx = tk.Text(width=30, height=5)
bt = tk.Button(text='selected range', command=get_selpoint)

[widget.pack() for widget in (lb, tx, bt)]

root.mainloop()
