# tk20.pyw

import tkinter as tk
root = tk.Tk()
strvar = tk.StringVar()
en = tk.Entry(textvariable=strvar)
strvar.set('HelloWorld')
en.pack()
root.mainloop()
