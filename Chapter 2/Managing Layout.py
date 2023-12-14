#Exercise 2A

import tkinter as tk

root = tk.Tk()

a_bttn = tk.Label(root, text="A", bg="red", relief="sunken", bd=5)
a_bttn.pack(side="top", expand = "YES", fill="x")
b_bttn = tk.Label(root, text="B", bg="yellow", relief="flat", bd=3, width=10)
b_bttn.pack(side="bottom", expand="NO")
c_bttn = tk.Label(root, text="C", bg="blue", relief="flat", bd=2, width=10)
c_bttn.pack(side="left", expand="YES", fill='none', anchor='se', padx=0)
d_bttn = tk.Label(root, text="D", bg="white", relief="flat", bd=2, width=10)
d_bttn.pack(side="right", expand="YES", fill='none', anchor='se', padx=0)
root.mainloop()

