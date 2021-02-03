import tkinter as tk

def btn_press():
    st_id = en1.get()
    st_name = en2.get()
    print(st_id, st_name)

root = tk.Tk()
lbl =tk.Label(text='Student ID')
en1 = tk.Entry()
lb2 = tk.Label(text='Name')
en2 = tk.Entry()
btn = tk.Button(text='set', command=btn_press)

[w.pack() for w in (lbl,en1,lb2,en2,btn)]
root.mainloop()