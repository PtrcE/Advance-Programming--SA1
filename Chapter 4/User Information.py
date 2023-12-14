import tkinter as tk
from tkinter import messagebox
import os

def on_click():
    name = name_entry.get()
    age = age_entry.get()
    hometown = hometown_entry.get()

    if not name or not age or not hometown:
        messagebox.showerror('Error', 'All fields are required.')
        return

    try:
        with open('bio.txt', 'w') as f:
            f.write(f'Name: {name}\n')
            f.write(f'Age: {age}\n')
            f.write(f'Hometown: {hometown}\n')
    except Exception as e:
        messagebox.showerror('Error', str(e))
        return

    messagebox.showinfo('Success', 'Data written to bio.txt.')

    try:
        with open('bio.txt', 'r') as f:
            data = f.read()
        messagebox.showinfo('Data', data)
    except Exception as e:
        messagebox.showerror('Error', str(e))

if os.path.exists('bio.txt'):
    os.remove('bio.txt')

root = tk.Tk()
root.title('Bio Data')

name_label = tk.Label(root, text='Name:')
name_entry = tk.Entry(root)

age_label = tk.Label(root, text='Age:')
age_entry = tk.Entry(root)

hometown_label = tk.Label(root, text='Hometown:')
hometown_entry = tk.Entry(root)

submit_button = tk.Button(root, text='Submit', command=on_click)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

age_label.grid(row=1, column=0)
age_entry.grid(row=1, column=1)

hometown_label.grid(row=2, column=0)
hometown_entry.grid(row=2, column=1)

submit_button.grid(row=3, column=1)

root.mainloop()